# 微控制器上的人工智能究竟如何工作：算子与内核

> **译者注**
> 本文深入浅出地揭示了 AI 模型在微控制器上运行的底层奥秘。它将“边缘 AI”从一个热门的营销术语，具象化为算子、内核与硬件指令的协同工作。对于希望在资源受限的嵌入式设备上榨干每一分性能的开发者而言，理解从通用 C++ 实现到利用 SIMD 指令，再到 NPU 专用硬件的逐级优化过程，是连接 AI 算法与硬件现实的关键桥梁，极具实践指导意义。

**原文链接：** [How AI on Microcontrollers Actually Works: Operators and Kernels](https://danielmangum.com/posts/ai-microcontrollers-operators-kernels/)

> **发布日期：** 2025年6月30日 · **阅读时长：** 约 13 分钟

关于“边缘 AI”的讨论热度早已是甚嚣尘上，尽管几乎每个人对它的理解都略有不同。但无论边缘 AI 对你意味着什么，一个普遍的共识是，执行推理的硬件通常在一个或多个维度上受到限制，无论是在计算能力、内存还是网络带宽方面。而在这些平台中，限制最严苛的或许就是微控制器（Microcontroller）。

我发现，虽然围绕在微控制器上“运行 AI”（即执行推理）的讨论很多，但关于这些系统实际能力以及新型硬件发展如何影响这一格局的信息却普遍匮乏。我希望通过这个系列文章，层层揭开术语的神秘面纱，探索从向模型输入数据到接收输出之间究竟发生了什么。在此过程中，我们将通过在真实的受限硬件上使用真实模型进行推理，来让我们的探索更加脚踏实地。

尽管在 AI 模型中，“权重”（weights）获得了绝大部分的关注，但仅有权重并**不足以**执行推理。根据模型的分发方式和所使用的运行时（runtime），模型可能会附带额外的数据或元数据，或者这些信息可能在与权重交互的软件中被明确定义。目前最适用于微控制器的运行时是 [**`tflite-micro` (Tensorflow Lite for Microcontrollers)**](https://ai.google.dev/edge/litert/microcontrollers/overview)，它是 [Tensorflow Lite](https://ai.google.dev/edge/litert) 的一个优化版本。

> **注意**：谷歌最近将 [Tensorflow Lite 更名为 LiteRT](https://developers.googleblog.com/en/tensorflow-lite-is-now-litert/)，并将 `tflite-micro` 更名为 LiteRT for Microcontrollers。

`tflite-micro` 使用 `.tflite` 文件格式，该格式通过 [FlatBuffers](https://flatbuffers.dev/) 对数据进行编码。与其他一些模型文件格式不同，`.tflite` 文件不仅包含封装了模型权重的张量（tensors），还包含了**计算图**（computation graph）。计算图会告知运行时在执行推理时该使用哪些操作。为了实现这一点，需要有一套预定义的**算子**（operators）。这在某种程度上类似于处理器[指令集架构（ISA）](https://en.wikipedia.org/wiki/Instruction_set_architecture)中定义的指令。对于 ISA，编译器会将高级编程语言映射到 ISA 中可用的指令上。TensorFlow 支持一套广泛的[内置算子](https://www.tensorflow.org/mlir/tf_ops)，而 TensorFlow Lite（以及 `tflite-micro`）则[只支持其中的一个子集](https://www.tensorflow.org/mlir/tfl_ops)。

延续这个类比，许多处理器实现了特定版本的 [Arm 架构](https://en.wikipedia.org/wiki/ARM_architecture_family)，但这并不意味着实现相同 ISA 的处理器就是等效的。每一个被支持的指令都必须在硬件中实现，而关于处理器如何设计的决策会从多个维度影响性能。同理，尽管 TensorFlow Lite 定义了一套算子，但这些算子的具体实现——即**内核**（kernels）——可能会有所不同。内核是在软件中实现的，但根据底层硬件的不同，一个内核的执行可能需要许多条指令，也可能被优化以利用专用的硬件支持。

一个简单的例子是[加法算子 (`TFL::AddOp`)](https://www.tensorflow.org/mlir/tfl_ops#tfladd_tfladdop)。我们将在未来的文章中介绍算子和内核是如何注册和调用的，但现在让我们先来看看 `tflite-micro` 中默认的加法算子逻辑。

[`tensorflow/lite/micro/kernels/add.cc`](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/kernels/add.cc#L168)

```cpp
TfLiteStatus AddEval(TfLiteContext* context, TfLiteNode* node) {
  auto* params = reinterpret_cast<TfLiteAddParams*>(node->builtin_data);

  TFLITE_DCHECK(node->user_data != nullptr);
  const OpDataAdd* data = static_cast<const OpDataAdd*>(node->user_data);

  const TfLiteEvalTensor* input1 =
      tflite::micro::GetEvalInput(context, node, kAddInputTensor1);
  const TfLiteEvalTensor* input2 =
      tflite::micro::GetEvalInput(context, node, kAddInputTensor2);
  TfLiteEvalTensor* output =
      tflite::micro::GetEvalOutput(context, node, kAddOutputTensor);

  if (output->type == kTfLiteFloat32 || output->type == kTfLiteInt32) {
    TF_LITE_ENSURE_OK(
        context, EvalAdd(context, node, params, data, input1, input2, output));
  } else if (output->type == kTfLiteInt8 || output->type == kTfLiteInt16) {
    TF_LITE_ENSURE_OK(context, EvalAddQuantized(context, node, params, data,
                                                input1, input2, output));
  } else {
    MicroPrintf("Type %s (%d) not supported.", TfLiteTypeGetName(output->type),
                output->type);
    return kTfLiteError;
  }

  return kTfLiteOk;
}

TFLMRegistration Register_ADD() {
  return tflite::micro::RegisterOp(AddInit, AddPrepare, AddEval);
}
```

从 `AddEval()` 函数中可以看出，我们期望的输出类型会影响算子的实现。为了说明底层硬件如何影响性能，让我们聚焦于期望输出为 `kTfLiteInt8`（有符号 8 位整数）或 `kTfLiteInt16`（有符号 16 位整数）的情况，这意味着我们将调用 `EvalAddQuantized()`。

[`tensorflow/lite/micro/kernels/add.cc`](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/kernels/add.cc#L91)

```cpp
TfLiteStatus EvalAddQuantized(TfLiteContext* context, TfLiteNode* node,
                              TfLiteAddParams* params, const OpDataAdd* data,
                              const TfLiteEvalTensor* input1,
                              const TfLiteEvalTensor* input2,
                              TfLiteEvalTensor* output) {
  tflite::ArithmeticParams op_params = {};
  op_params.left_shift = data->left_shift;
  op_params.input1_offset = data->input1_offset;
  op_params.input1_multiplier = data->input1_multiplier;
  op_params.input1_shift = data->input1_shift;
  op_params.input2_offset = data->input2_offset;
  op_params.input2_multiplier = data->input2_multiplier;
  op_params.input2_shift = data->input2_shift;
  op_params.output_offset = data->output_offset;
  op_params.output_multiplier = data->output_multiplier;
  op_params.output_shift = data->output_shift;
  SetActivationParams(data->output_activation_min, data->output_activation_max,
                      &op_params);
  bool need_broadcast = reference_ops::ProcessBroadcastShapes(
      tflite::micro::GetTensorShape(input1),
      tflite::micro::GetTensorShape(input2), &op_params);

  switch (output->type) {
    case kTfLiteInt8: {
      if (need_broadcast) {
        reference_integer_ops::BroadcastAdd4DSlow(
            op_params, tflite::micro::GetTensorShape(input1),
            tflite::micro::GetTensorData<int8_t>(input1),
            tflite::micro::GetTensorShape(input2),
            tflite::micro::GetTensorData<int8_t>(input2),
            tflite::micro::GetTensorShape(output),
            tflite::micro::GetTensorData<int8_t>(output));
      } else {
        reference_integer_ops::Add(
            op_params, tflite::micro::GetTensorShape(input1),
            tflite::micro::GetTensorData<int8_t>(input1),
            tflite::micro::GetTensorShape(input2),
            tflite::micro::GetTensorData<int8_t>(input2),
            tflite::micro::GetTensorShape(output),
            tflite::micro::GetTensorData<int8_t>(output));
      }
      break;
    }
    case kTfLiteInt16: {
      if (need_broadcast) {
        reference_ops::BroadcastAdd4DSlow(
            op_params, tflite::micro::GetTensorShape(input1),
            tflite::micro::GetTensorData<int16_t>(input1),
            tflite::micro::GetTensorShape(input2),
            tflite::micro::GetTensorData<int16_t>(input2),
            tflite::micro::GetTensorShape(output),
            tflite::micro::GetTensorData<int16_t>(output));
      } else {
        reference_ops::Add(op_params, tflite::micro::GetTensorShape(input1),
                           tflite::micro::GetTensorData<int16_t>(input1),
                           tflite::micro::GetTensorShape(input2),
                           tflite::micro::GetTensorData<int16_t>(input2),
                           tflite::micro::GetTensorShape(output),
                           tflite::micro::GetTensorData<int16_t>(output),
                           false);
      }
      break;
    }
    default:
      MicroPrintf("Type %s (%d) not supported.",
                  TfLiteTypeGetName(output->type), output->type);
      return kTfLiteError;
  }

  return kTfLiteOk;
}
```
当输出类型为 `kTfLiteInt8` 且不需要广播（broadcast）时，我们会调用 `reference_integer_ops::Add()`。

> “广播”（Broadcasting）是使数组具有兼容形状以进行算术运算的过程。例如，[矩阵加法](https://en.wikipedia.org/wiki/Matrix_addition)要求两个输入矩阵具有相同的维度。

[`tensorflow/lite/kernels/internal/reference/add.h`](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/kernels/internal/reference/add.h#L31)

```cpp
template <typename T>
inline void Add(const ArithmeticParams& params,
                const RuntimeShape& input1_shape, const T* input1_data,
                const RuntimeShape& input2_shape, const T* input2_data,
                const RuntimeShape& output_shape, T* output_data) {
  T activation_min, activation_max;
  GetActivationParams(params, &activation_min, &activation_max);

  const int flat_size =
      MatchingElementsSize(input1_shape, input2_shape, output_shape);
  for (int i = 0; i < flat_size; ++i) {
    output_data[i] = ActivationFunctionWithMinMax(
        input1_data[i] + input2_data[i], activation_min, activation_max);
  }
}
```
你可能已经猜到，这个实现基本上就是遍历两个输入张量并执行 `input1_data[i] + input2_data[i]`。这可以被看作是一种“最通用的”实现，因为它不利用任何特定于硬件的功能；任何处理器都可以执行顺序加法。然而，正如[图形处理单元（GPU）](https://en.wikipedia.org/wiki/Graphics_processing_unit)市场近乎无限的需求所证明的那样，通过在硬件中并行化操作可以获得巨大的性能提升。幸运的是，许多执行推理所需的操作都是[“易于并行”的（embarrassingly parallel）](https://en.wikipedia.org/wiki/Embarrassingly_parallel)。例如，我们可以将处理器指向两个输入，如果硬件支持，整个矩阵加法操作可能在“一个”周期内完成，而不是通过迭代张量来执行顺序加法，后者可能需要许多处理器周期。

> 这个操作实际上不太可能只花费一个周期，考虑到现代处理器的复杂性，但关键在于，整个操作的运行时间可以减少到与顺序加法实现中一步操作相同数量级的周期。

显然，微控制器没有像云服务提供商数据中心里安装的那种巨型 GPU。然而，许多微控制器确实实现了能够加速这些常见操作的架构扩展。由于 TensorFlow Lite 允许使用不同的内核实现，因此在支持的情况下，可以利用这种硬件加速。

许多微控制器实现了 [Arm Cortex-M](https://en.wikipedia.org/wiki/ARM_Cortex-M) 核心。例如，像树莓派 [RP2350](https://www.raspberrypi.com/products/rp2350/) 和 Nordic Semiconductor 的 [nRF54H20](https://www.nordicsemi.com/Products/nRF54H20) 这样的芯片都实现了多个 Arm [Cortex-M33](https://en.wikipedia.org/wiki/ARM_Cortex-M#Cortex-M33) 核心。前者实现了 Armv8-M 数字信号处理（DSP）扩展，增加了对[单指令多数据（SIMD）](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)指令的支持。功能更强大的芯片，如 [Alif Ensemble E3](https://alifsemi.com/ensemble-e3-series/)，则实现了 [Cortex-M55](https://en.wikipedia.org/wiki/ARM_Cortex-M#Cortex-M55) 核心，支持 Armv8-M 向量扩展（MVE），也被称为 [Arm Helium](https://www.arm.com/technologies/helium)。E3 芯片还以 [Arm Ethos-U 神经网络处理单元（NPU）](https://developer.arm.com/documentation/109267/0102/Arm-Ethos-U-NPU)的形式包含了专用加速器。

Arm 提供了相应的软件，允许支持这些扩展中的一个或多个的硬件来加速 TensorFlow Lite 内核的实现。例如，[CMSIS-NN](https://github.com/ARM-software/CMSIS-NN) 库提供了多种内核实现：不利用优化的（即[纯 C 实现](https://github.com/ARM-software/CMSIS-NN?tab=readme-ov-file#pure-c)），[仅利用 DSP 扩展的](https://github.com/ARM-software/CMSIS-NN?tab=readme-ov-file#dsp-extension)，或[利用 MVE 扩展的](https://github.com/ARM-software/CMSIS-NN?tab=readme-ov-file#mve-extension)（这需要 DSP 扩展的实现）。TensorFlow Lite 拥有集成了 CMSIS-NN 功能的内核“移植”。让我们来看看在使用 CMSIS-NN 内核时，加法操作有何不同。

[设置过程](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/kernels/cmsis_nn/add.cc#L408)看起来与我们观察到的第一个加法操作内核大体相同。然而，当我们进入 `EvalAddQuantizedInt8()` 时，就可以开始看到硬件加速是如何被利用的。

[`tensorflow/lite/micro/kernels/cmsis_nn/add.cc`](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/kernels/cmsis_nn/add.cc#L124)

```cpp
TfLiteStatus EvalAddQuantizedInt8(TfLiteContext* context, TfLiteNode* node,
                                  TfLiteAddParams* params, const OpData* data,
                                  const TfLiteEvalTensor* input1,
                                  const TfLiteEvalTensor* input2,
                                  TfLiteEvalTensor* output) {
  tflite::ArithmeticParams op_params;
  UpdateOpParams(&op_params, data);

  bool need_broadcast = reference_ops::ProcessBroadcastShapes(
      tflite::micro::GetTensorShape(input1),
      tflite::micro::GetTensorShape(input2), &op_params);

  if (need_broadcast) {
    reference_integer_ops::BroadcastAdd4DSlow(
        op_params, tflite::micro::GetTensorShape(input1),
        tflite::micro::GetTensorData<int8_t>(input1),
        tflite::micro::GetTensorShape(input2),
        tflite::micro::GetTensorData<int8_t>(input2),
        tflite::micro::GetTensorShape(output),
        tflite::micro::GetTensorData<int8_t>(output));
  } else {
    arm_elementwise_add_s8(
        tflite::micro::GetTensorData<int8_t>(input1),

        tflite::micro::GetTensorData<int8_t>(input2), op_params.input1_offset,
        op_params.input1_multiplier, op_params.input1_shift,
        op_params.input2_offset, op_params.input2_multiplier,
        op_params.input2_shift, op_params.left_shift,
        tflite::micro::GetTensorData<int8_t>(output), op_params.output_offset,
        op_params.output_multiplier, op_params.output_shift,
        op_params.quantized_activation_min, op_params.quantized_activation_max,
        MatchingElementsSize(tflite::micro::GetTensorShape(input1),
                             tflite::micro::GetTensorShape(input2),
                             tflite::micro::GetTensorShape(output)));
  }

  return kTfLiteOk;
}
```
`arm_elementwise_add_s8()` 函数由 CMSIS-NN 提供，其实现会根据可用的硬件扩展来利用不同的硬件功能。

[`Source/BasicMathFunctions/arm_elementwise_add_s8.c`](https://github.com/ARM-software/CMSIS-NN/blob/dbcb869c2f147f89f661f977cb8687b5a656a841/Source/BasicMathFunctions/arm_elementwise_add_s8.c#L52)

```c
arm_cmsis_nn_status arm_elementwise_add_s8(const int8_t *input_1_vect,
                                           const int8_t *input_2_vect,
                                           const int32_t input_1_offset,
                                           const int32_t input_1_mult,
                                           const int32_t input_1_shift,
                                           const int32_t input_2_offset,
                                           const int32_t input_2_mult,
                                           const int32_t input_2_shift,
                                           const int32_t left_shift,
                                           int8_t *output,
                                           const int32_t out_offset,
                                           const int32_t out_mult,
                                           const int32_t out_shift,
                                           const int32_t out_activation_min,
                                           const int32_t out_activation_max,
                                           const int32_t block_size)
{
#if defined(ARM_MATH_MVEI)
    // ... MVE 向量指令实现 ...
    int32_t count = block_size;

    while (count > 0)
    {
        int32x4_t vect_1;
        int32x4_t vect_2;

        mve_pred16_t p = vctp32q((uint32_t)count);

        vect_1 = vldrbq_z_s32(input_1_vect, p);
        vect_2 = vldrbq_z_s32(input_2_vect, p);

        vect_1 = vaddq_s32(vect_1, vdupq_n_s32(input_1_offset));
        vect_2 = vaddq_s32(vect_2, vdupq_n_s32(input_2_offset));

        // ... (省略部分代码)

        vect_1 = vaddq_s32(vect_1, vect_2); // 向量加法指令

        // ... (省略部分代码)

        input_1_vect += 4;
        input_2_vect += 4;
        vstrbq_p_s32(output, vect_1, p);

        output += 4;
        count -= 4;
    }
#else
    // ... 非 MVE 实现 ...
    #if defined(ARM_MATH_DSP)
    // ... DSP 指令实现 ...
    int32_t a_1, b_1, a_2, b_2;
    // ...
    loop_count = block_size >> 2;

    while (loop_count > 0)
    {
        // ... (省略部分代码)
        a_1 = SADD16(a_1, offset_1_packed); // 16位并行加法指令
        b_1 = SADD16(b_1, offset_1_packed);

        a_2 = SADD16(a_2, offset_2_packed);
        b_2 = SADD16(b_2, offset_2_packed);
        // ... (省略部分代码)
        loop_count--;
    }

    loop_count = block_size & 0x3;
    #else
    // ... 纯 C 实现 ...
    loop_count = block_size;
    #endif

    while (loop_count > 0)
    {
        /* C = A + B */
        // ... (此处为逐元素相加的循环)
        loop_count--;
    }

#endif /* ARM_MATH_MVEI */

    return (ARM_CMSIS_NN_SUCCESS);
}
```
例如，如果存在 DSP 扩展，代码会使用该扩展提供的并行有符号 16 位加法指令（`SADD16`），通过将 8 位有符号整数打包到 16 位参数中，然后在一次迭代中计算 4 个输出来减少必要的循环次数。如果存在 MVE 扩展，则可以直接使用向量加法指令（`VADD`），使计算效率更高。

这些优化在编译 `tflite-micro` 时通过配置项启用。它们可以应用于任何使用这些算子的模型，而无需在从一种架构迁移到另一种架构时修改模型。然而，某些优化确实需要修改模型。例如，当使用包含 Arm Ethos-U NPU 的微控制器（如前面提到的 Alif Ensemble E3）时，你可以通过 [Vela 编译器](https://developer.arm.com/documentation/109267/0102/Tool-support-for-the-Arm-Ethos-U-NPU/Ethos-U-Vela-compiler)来处理 `.tflite` 模型。转换后的模型会将内置算子序列替换为一个自定义的 [`ETHOSU` 算子](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/micro_mutable_op_resolver.h#L258)和一个[命令流（command stream）](https://developer.arm.com/documentation/102420/0200/Programmers-model/Command-stream?lang=en)。应用处理器会通知 NPU 命令流的地址和其他相关数据，然后触发它执行推理。

与加法算子不同，`ETHOSU` 算子没有备用的“回退”内核实现；通过 Vela 编译器转换的模型无法在没有 Ethos-U NPU 的微控制器上运行。对于那些拥有该 NPU 的设备，我们可以在 `ETHOSU` 自定义算子的 `Eval()` 实现中看到前面描述的逻辑。

[`tensorflow/lite/micro/kernels/ethos_u/ethosu.cc`](https://github.com/tensorflow/tflite-micro/blob/3200ccd18268346d0ea965720c5599a3d051e853/tensorflow/lite/micro/kernels/ethos_u/ethosu.cc)

```cpp
TfLiteStatus Eval(TfLiteContext* context, TfLiteNode* node) {
  // ... (省略部分代码)

  // Get command stream data address.
  tensor = context->GetEvalTensor(context, node->inputs->data[0]);
  cms_data = reinterpret_cast<void*>(tensor->data.uint8);

  // Get addresses to weights/scratch/input data.
  // ... (省略获取地址的代码)
  
  // ...
  // 这段代码将这样分配 NPU 的基地址：
  //
  // +--------------+----------------------+
  // | 基地址       | 描述                 |
  // +--------------+----------------------+
  // |            0 | TFLM 模型            |
  // |            1 | TFLM arena           |
  // |            2 | Ethos-U 快速暂存区   |
  // |         3..n | 输入张量             |
  // |         n..m | 输出张量             |
  // +--------------+----------------------+
  //
  // ...

  struct ethosu_driver* drv = ethosu_reserve_driver();
  result = ethosu_invoke_v3(drv, cms_data, data->cms_data_size, base_addrs,
                            base_addrs_size, num_tensors,
                            GetMicroContext(context)->external_context());
  ethosu_release_driver(drv);

  if (-1 == result) {
    return kTfLiteError;
  } else {
    return kTfLiteOk;
  }
}
```

至此，我们已经看到了算子优化的完整光谱：从纯 C 实现的内核，到利用架构扩展中硬件指令的内核，再到将推理任务完全卸载给一个独立处理器的内核。在未来的文章中，我们将探讨算子是如何在 `.tflite` 文件中编码的，以及运行时最终是如何调用底层内核的。

---

# 思维碰撞

看完这篇硬核的技术拆解，你是否对微控制器上的 AI 有了更深的理解？欢迎在评论区分享你的想法：

1.  你是否在自己的项目中使用过 TinyML 或边缘 AI 技术？遇到过哪些性能瓶颈或有趣的挑战？
2.  文章中提到的从纯 C 实现、DSP/MVE 优化到 NPU 加速，你认为哪种方案在未来嵌入式领域更有前景？为什么？
3.  除了文中提到的 Arm 架构扩展和 NPU，你还了解哪些用于加速嵌入式 AI 的硬件或软件技术？
4.  对于刚入门 TinyML 的开发者，你有什么学习建议或推荐的硬件平台吗？