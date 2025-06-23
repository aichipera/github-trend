
# [Python 现在可以调用 Mojo 代码了](20250623-python_run_mojo.mp3)

> 作者：**Vincent**，原文地址：https://koaning.io/posts/giving-mojo-a-spin/

> **译者注**: Mojo 是由 LLVM 之父 Chris Lattner 团队推出的新语言，旨在成为 Python 的超集，兼顾易用性与高性能。近期，Mojo 实现了与 Python 的直接互操作，允许 Python 无缝调用 Mojo 模块。这意味着开发者无需重写整个项目，只需将性能瓶颈用 Mojo 实现，即可获得巨大性能提升。这极大地降低了迁移门槛，虽然目前尚处早期阶段，但其展现的潜力已非常激动人心。


[Chris Lattner](https://www.nondot.org/sabre/) [最近在一次分享中提到](https://www.youtube.com/watch?v=04_gN-C9IAo&list=PLWEAb1SXhjlfkEF_PxzYHonU_v5LPMI8L&index=1)，Python 现在已经可以实际调用 Mojo 代码了。我超爱这个想法！因为我正需要一门简单的编译型语言，来为 Python 提供一些真正高速的函数。于是，我赶紧上手试了一下。

## 环境搭建

环境搭建过程比我记忆中要简单得多，现在你可以用 `uv` 来完成。

```text
uv pip install modular --index-url https://dl.modular.com/public/nightly/python/simple/
```

安装完毕后，你可以声明一个 `.mojo` 文件，内容如下：

```python
# mojo_module.mojo
from python import PythonObject
from python.bindings import PythonModuleBuilder
import math
from os import abort

@export
fn PyInit_mojo_module() -> PythonObject:
    try:
        var m = PythonModuleBuilder("mojo_module")
        m.def_function[factorial]("factorial", docstring="计算 n 的阶乘")
        return m.finalize()
    except e:
        return abort[PythonObject](String("创建 Python Mojo 模块时出错:", e))

fn factorial(py_obj: PythonObject) raises -> PythonObject:
    # 如果 `py_obj` 无法转换为 Mojo 的 `Int` 类型，将抛出异常。
    var n = Int(py_obj)

    var result = 1
    for i in range(1, n + 1):
        result *= i

    return result
```

然后，你就可以在 Python 中这样加载它：

```python
# main.py
import max.mojo.importer
import os
import sys
import time 
import math
sys.path.insert(0, "") # 确保当前目录在搜索路径中

import mojo_module

start = time.time()
print(mojo_module.factorial(10))
end = time.time()
print(f"Mojo 耗时: {end - start} 秒")

start = time.time()
print(math.factorial(10))
end = time.time()
print(f"Python 耗时: {end - start} 秒")
```

这是当时的输出结果：

```text
3628800
Mojo 耗时: 3.0279159545898438e-05 秒
3628800
Python 耗时: 5.0067901611328125e-06 秒
```

这一切都能正常工作，但在我写这篇博客时，我还是发现了一些尚未打磨好的地方。如果我把阶乘的数字增加到 100，输出就变了。

```text
0
Mojo 耗时: 2.7894973754882812e-05 秒
1882677176888926099743767702491600857595403648714924258875982315083531563316135988668829328894959231336464054459300577406301619193413805978188834575585470555243263755650071317708800000000000000000000000000000
Python 耗时: 9.298324584960938e-06 秒
```

这很可能是因为 Modular（Mojo 的开发公司）那边的整数溢出问题。文档里也提到，整个技术栈还处于非常早期的阶段，我想这就是一个迹象。

## 另一个例子

考虑到溢出问题可能是关键，我决定再运行一个例子，看看我们是否能测量到速度上的提升。这次我选择了一个朴素的质数计数示例。这是 Mojo 代码：

```python
# mojo_module.mojo
from python import PythonObject
from python.bindings import PythonModuleBuilder
import math
from os import abort

@export
fn PyInit_mojo_module() -> PythonObject:
    try:
        var m = PythonModuleBuilder("mojo_module")
        m.def_function[count_primes]("count_primes", docstring="计算直到 n 的所有质数")
        return m.finalize()
    except e:
        return abort[PythonObject](String("创建 Python Mojo 模块时出错:", e))

fn count_primes(py_obj: PythonObject) raises -> PythonObject:
    var n = Int(py_obj)
    var count: Int = 0
    for i in range(2, n + 1):
        var is_prime: Bool = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
```

这是 Python 代码，请注意，我还加入了一个 NumPy 实现用于对比。

```python
# main.py
import numpy as np
import max.mojo.importer
import os
import sys
import time 
import math
sys.path.insert(0, "") # 确保当前目录在搜索路径中

import mojo_module

def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

# 一个欠佳的 NumPy 实现，仅为对比
def count_primes_numpy(n):
    if n < 2:
        return 0
    
    candidates = np.arange(2, n + 1)
    is_prime_mask = np.ones(len(candidates), dtype=bool)
    
    for idx, candidate in enumerate(candidates):
        if candidate == 2:
            continue
        
        divisors = np.arange(2, candidate)
        has_divisor = np.any(candidate % divisors == 0)
        
        if has_divisor:
            is_prime_mask[idx] = False
    
    return np.sum(is_prime_mask)

n = 20_000

start = time.time()
print(count_primes(n))
end = time.time()
print(f"Python 耗时: {end - start} 秒")

start = time.time()
print(count_primes_numpy(n))
end = time.time()
print(f"Numpy 耗时: {end - start} 秒")

start = time.time()
print(mojo_module.count_primes(n))
end = time.time()
print(f"Mojo 耗时: {end - start} 秒")
```

结果看起来相当有前景！

```text
2262
Python 耗时: 0.44585609436035156 秒
2262
Numpy 耗时: 0.25995898246765137 秒
2262
Mojo 耗时: 0.011101961135864258 秒
```

当然，有比我这里用的更好的质数计数算法，所以请对这个结果持保留态度，但这真的**非常**激动人心。Mojo 比 Rust 容易学得多，但我似乎得到了我想要（且需要）的函数加速效果。

在写这篇文章的时候，主要的缺点是 Modular 的技术栈还处于[早期阶段](https://docs.modular.com/mojo/manual/python/mojo-from-python/#known-limitations)，不过官方似乎也为[构建这些扩展](https://docs.modular.com/mojo/manual/python/mojo-from-python/#building-mojo-extension-modules)提供了一些初步支持。

简而言之：它目前还不适合正式投入生产环境，但我现在更加乐观了，那个梦想（Python 的性能自由）似乎越来越触手可及了！

---

# Hacker News 网友热议

> 📰 **Hacker News 讨论帖** 👉 https://news.ycombinator.com/item?id=44331316


## 核心争议：从“Python超集”到“Pythonic语言”

许多评论者对Mojo的定位转变表示质疑。Mojo最初以“Python的超集”为旗号，并以此获得了大量VC投资，这让开发者期待能无缝地在现有Python代码中逐步引入Mojo进行性能优化。然而，如今Mojo的宣传更偏向于“一种具有Python风格的语言”，这让社区感觉其最初的承诺已被削弱。有评论认为，这更像是一种为了融资而采取的营销策略。如果Python程序员仍需学习所有权、生命周期和编译时（comptime）等复杂新概念，那么Mojo与学习Rust或C++相比，仅仅语法相似的优势就显得不那么突出了。

## 技术实现与价值：这只是又一个Cython吗？

对于“Python现在可以运行Mojo代码”这一进展，部分网友指出，其本质是通过创建Python绑定来调用预编译的Mojo函数，这与现有的C/C++扩展、Cython或Nim等技术在原理上并无二致，算不上是革命性的成就。有人认为，Mojo的真正目标之一就是成为Cython的更优替代品，提供更现代的工具链和对GPU等硬件的直接访问。值得一提的是，Cython的创始人也在此次讨论中表示了对此的认同。

## 最大的障碍：闭源现状

Mojo编译器目前仍是闭源的，这一点成为社区采纳它的最大阻碍。许多开发者明确表示，在Mojo于2026年按计划开源之前，他们不会投入时间学习，更不会将其用于任何生产环境。这种封闭性让一些人联想到了Jonathan Blow的Jai语言，认为一个无法被社区完全审查和使用的语言难以获得成功。

## 竞争格局与未来前景

评论者认为Mojo面临着激烈的市场竞争。一方面，NVIDIA正在大力推广其自家的CUDA Python工具链，为Python开发者提供直接的GPU编程能力。另一方面，Julia语言作为一个更成熟的、在科研和金融领域已有广泛应用的备选方案，也提供了强大的性能和成熟的生态系统。

尽管如此，仍有许多人对Mojo寄予厚望。他们认为Mojo的真正潜力在于其由Chris Lattner（LLVM、Clang、Swift、MLIR的创造者）领导，并深度整合了MLIR。其最终目标是打破NVIDIA CUDA的生态壁垒，提供一种能在CPU、NVIDIA GPU、AMD GPU等多种硬件上高效运行的统一编程模型，尤其是在AI推理领域。Modular公司获得的1.3亿美元融资，目标也并非仅仅是创造一门语言，而是要革新整个AI基础设施。

## 学习曲线与开发者生态

关于学习曲线的讨论也十分热烈。有开发者认为，从Python转向Mojo，虽然需要学习新概念，但比起直接学习C/C++的巨大鸿沟（包括处理头文件、编译器和复杂的构建系统），Mojo提供了一个更平滑的过渡路径。但也有人反驳称，C语言本身比Rust等现代系统语言简单得多，不应过分夸大其学习难度。总的来说，开发者普遍认为，现代语言的工具链和生态系统（如依赖管理）是比语法本身更重要的考量因素，而这正是C/C++的痛点之一，也是Mojo、Rust和Zig等新语言试图解决的问题。

---

# 思维碰撞区

这篇文章的测试结果确实让人眼前一亮，Mojo 在计算密集型任务上展现了惊人的潜力。这不禁让我们思考：

1.  **Mojo vs. Cython/Numba/Rust：** 你认为 Mojo 与现有的 Python 加速方案（如 Cython、Numba 或用 Rust/C++ 写扩展）相比，最大的优势和劣势是什么？它会成为未来的主流选择吗？
2.  **应用场景畅想：** 除了文中的数值计算，你觉得还有哪些场景特别适合用 Mojo 来优化 Python 代码？（例如：图像处理、数据清洗、复杂的循环逻辑等）
3.  **你的实践经历：** 你是否也尝试过 Mojo？遇到了哪些有趣的问题或惊喜的发现？欢迎分享你的“踩坑”或“寻宝”经历！
