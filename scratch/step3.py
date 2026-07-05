import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Embedding-Layers\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

badges_html = """<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <!-- MORE BADGES HERE -->
</p>"""

# Add after banner
if '<!-- MORE BADGES HERE -->' not in content:
    content = content.replace('</p>\n\n# 🌌', '</p>\n\n' + badges_html + '\n\n# 🌌')

# SEO optimization: Add keywords and description right below the title
seo_text = """
<div align="center">
  <strong>Comprehensive Curated List of Embedding Layers in Artificial Intelligence, Machine Learning, and Deep Learning</strong>
  <br>
  <em>Keywords: AI, Machine Learning, Embedding Layers, Vector Database, LLM, Neural Networks, Deep Learning, Vision Transformers, RoPE</em>
</div>
"""
if "Comprehensive Curated List" not in content:
    content = content.replace('# 🌌 Awesome-Embedding-Layers\n', '# 🌌 Awesome-Embedding-Layers\n' + seo_text)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Step 3 completed")
