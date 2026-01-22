from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            title_text = line[2:]
            return title_text.strip()
    
    raise Exception("No header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    opened_file = open(from_path)
    read_file = opened_file.read()
    opened_file.close()

    o_file = open(template_path)
    r_file = o_file.read()
    o_file.close()

    html_node = markdown_to_html_node(read_file)
    html_string = html_node.to_html()

    title = extract_title(read_file)
    new_title = r_file.replace("{{ Title }}", title)
    content = new_title.replace("{{ Content }}", html_string)

    directory_path = os.path.dirname(dest_path)
    if directory_path != "":
        directory = os.makedirs(directory_path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(content)
    file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_dir_content):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path):
            if entry_path.endswith(".md"):
                relative_path = os.path.relpath(entry_path, root_dir_content)
                dest_path = os.path.join(dest_dir_path, relative_path)
                dest_path = dest_path[:-3] + ".html"
                generate_page(entry_path, template_path, dest_path)
        else:
            generate_pages_recursive(entry_path, template_path, dest_dir_path, root_dir_content)