import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Embedding-Layers\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('chartrepos', 'chart?repos')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Step 6 completed")
