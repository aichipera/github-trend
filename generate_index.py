import os
from datetime import datetime
from collections import defaultdict
from bs4 import BeautifulSoup  # 需要先安装: pip install beautifulsoup4

def extract_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            return soup.title.string if soup.title else None
    except:
        return None

def find_ppt_files():
    categories = ['daily', 'weekly', 'monthly']
    files_dict = defaultdict(list)
    
    for category in categories:
        category_path = os.path.join(os.path.dirname(__file__), category)
        if os.path.exists(category_path):
            for root, _, files in os.walk(category_path):
                for file in files:
                    if file.endswith('ppt.html'):
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(root, os.path.dirname(__file__))
                        title = extract_title(file_path) or file
                        files_dict[category].append({
                            'path': f'{rel_path}/{file}',
                            'name': file,
                            'title': title,
                            'date': os.path.getmtime(file_path)
                        })
    
    for category in files_dict:
        files_dict[category].sort(key=lambda x: x['date'], reverse=True)
    
    return files_dict

def generate_html(files_dict):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Trends Summary</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <header class="mb-12">
            <h1 class="text-4xl font-bold text-gray-900 mb-4">GitHub Trends Summary</h1>
            <p class="text-gray-600">A collection of GitHub trending repositories analysis</p>
        </header>
        <main class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
"""
    
    for category in ['daily', 'weekly', 'monthly']:
        if category in files_dict:
            html += f"""
            <section class="bg-white rounded-lg shadow-lg p-6">
                <h2 class="text-2xl font-semibold text-gray-800 mb-4">{category.title()} Reports</h2>
                <ul class="space-y-3">"""
                
            for file in files_dict[category]:
                date_str = datetime.fromtimestamp(file['date']).strftime('%Y-%m-%d')
                html += f"""
                    <li class="group">
                        <a href="{file['path']}" class="block p-3 rounded-md hover:bg-gray-50 transition-colors">
                            <time class="text-sm text-gray-500">{date_str}</time>
                            <h3 class="text-gray-900 group-hover:text-blue-600 font-medium">{file['title']}</h3>
                        </a>
                    </li>"""
                
            html += """
                </ul>
            </section>"""
    
    html += """
        </main>
        <footer class="mt-12 text-center text-gray-600 text-sm">
            <p>Generated at {}</p>
        </footer>
    </div>
</body>
</html>""".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    files = find_ppt_files()
    generate_html(files)
    print("index.html has been generated successfully!")
