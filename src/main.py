from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from functions import text_to_textnodes
from copystatic import copy_static
from gencontent import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", "content", base_path)

    #root = markdown_to_html_node(md)
    #print(root.to_html())
    
    #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev" )
    #print(node)





main()