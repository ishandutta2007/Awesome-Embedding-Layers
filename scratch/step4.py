import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Embedding-Layers\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

follower_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

if follower_badge not in content:
    content = content.replace('<!-- MORE BADGES HERE -->', follower_badge + '\n  <!-- MORE BADGES HERE -->')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Step 4 completed")
