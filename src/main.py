from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from functions import text_to_textnodes
from copystatic import copy_static
from gencontent import generate_pages_recursive

def main():

    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public", "content")

    #root = markdown_to_html_node(md)
    #print(root.to_html())
    
    #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev" )
    #print(node)





main()