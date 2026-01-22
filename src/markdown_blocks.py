from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from functions import text_to_textnodes



class BlockType(Enum):

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
 
    blocks = markdown.split("\n\n")
    no_white_space = []

    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            no_white_space.append(stripped)
    
    return no_white_space

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
   
    if len(lines) > 1 and lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE
    
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> ") and not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            inline_children = [text_node_to_html_node(tn) for tn in text_nodes]
            p_child = ParentNode("p", inline_children)
            children.append(p_child)
        
        elif block_type == BlockType.HEADING:
            hash_count = 0
            for ch in block:
                if ch == "#":
                    hash_count += 1
                else:
                    break
            heading_text = block[hash_count:].lstrip()
            text_nodes = text_to_textnodes(heading_text)
            inline_children = [text_node_to_html_node(tn) for tn in text_nodes]
            tag = f"h{hash_count}"
            heading_node = ParentNode(tag, inline_children)
            children.append(heading_node)

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped_lines = []
            for line in lines:
                if line.startswith("> "):
                    stripped_lines.append(line[2:])
                elif line.startswith(">"):
                    stripped_lines.append(line[1:])
                else:
                    stripped_lines.append(line)
            quote_text = "\n".join(stripped_lines)
            text_nodes = text_to_textnodes(quote_text)
            inline_children = [text_node_to_html_node(tn) for tn in text_nodes]
            quote_node = ParentNode("blockquote", inline_children)
            children.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []

            for line in lines:
                item_text = line[2:] if line.startswith("- ") else line
                text_nodes = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", inline_children)
                li_nodes.append(li_node)
            ul_node = ParentNode("ul", li_nodes)
            children.append(ul_node)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []

            for line in lines:
                parts = line.split(". ", 1)
                if len(parts) == 2:
                    item_text = parts[1]
                else:
                    item_text = line
                text_nodes = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", inline_children)
                li_nodes.append(li_node)
            ol_node = ParentNode("ol", li_nodes)
            children.append(ol_node)
        
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            code_content = "\n".join(lines[1:-1]) + "\n"
            code_leaf = LeafNode(None, code_content)
            code_node = ParentNode("code", [code_leaf])
            pre_node = ParentNode("pre", [code_node])
            children.append(pre_node)

    root = ParentNode("div", children)
    return root


