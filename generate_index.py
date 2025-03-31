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
        <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl p-6 mb-8 shadow-lg">
            <a href="https://github.com/aichipera/github-trend" 
               class="flex items-center justify-center space-x-3 text-white text-xl hover:text-blue-100 transition-colors">
               <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
                 <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
               </svg>
               <span>View this project on GitHub</span>
               <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
               </svg>
            </a>
        </div>
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
