import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def generate_page_recursive(dir_path_content, template_path, dir_path_dest):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dir_path_dest, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(
                from_path,
                template_path,
                dest_path,
            )
        else:
            generate_page_recursive(from_path, template_path, dest_path)


def generate_page(content_dir_path, template_path, dest_path):
    print(f"Generating page from {content_dir_path} to {dest_path} using {template_path}")
    content = open(content_dir_path, "r")
    markdown_content = content.read()
    content.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
