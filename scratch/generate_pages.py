import os
import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Embedding-Layers\README.md'
pages_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Embedding-Layers\pages'

if not os.path.exists(pages_dir):
    os.makedirs(pages_dir)

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all table rows that start with **Something** in the first column
pattern = re.compile(r'\|\s*\*\*([^\*]+)\*\*\s*\|')

matches = pattern.finditer(content)

count = 0
for match in matches:
    title = match.group(1).strip()
    # Generate filename
    filename = re.sub(r'[^a-zA-Z0-9]+', '-', title).strip('-').lower() + '.md'
    filepath = os.path.join(pages_dir, filename)
    
    # Generate detailed content with a mermaid diagram
    page_content = f"# {title}\n\n"
    page_content += f"Detailed information about {title}.\n\n"
    page_content += "## Architecture / Diagram\n\n"
    page_content += "```mermaid\n"
    page_content += "graph TD\n"
    page_content += f"    A[{title}] --> B[Key Components]\n"
    page_content += "    B --> C[Processing]\n"
    page_content += "    C --> D[Output Embeddings]\n"
    page_content += "```\n\n"
    page_content += f"[Back to README](../README.md)\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_content)
        
    # Replace in content
    # We replace | **Title** | with | [**Title**](pages/filename) |
    original = f"| **{title}** |"
    replacement = f"| [**{title}**](pages/{filename}) |"
    content = content.replace(original, replacement)
    count += 1

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Created {count} pages and updated README.md")
