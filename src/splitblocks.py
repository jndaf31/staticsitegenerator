from enum import Enum
from htmlnode import ParentNode, HTMLNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType
from splitnodes import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.HEADING:
                tag = ''
                clean_block = ''
                if block.startswith('# '): 
                    tag = 'h1'
                    clean_block = block[2:]
                elif block.startswith('## '): 
                    tag = 'h2'
                    clean_block = block[3:]
                elif block.startswith('### '): 
                    tag = 'h3'
                    clean_block = block[4:]
                elif block.startswith('#### '): 
                    tag = 'h4'
                    clean_block = block[5:]
                elif block.startswith('##### '): 
                    tag = 'h5'
                    clean_block = block[6:]
                elif block.startswith('###### '): 
                    tag = 'h6'
                    clean_block = block[7:]
                children.append(ParentNode(tag,text_to_children(clean_block)))

            case BlockType.PARAGRAPH:
                clean_block = block.replace('\n', ' ')
                children.append(ParentNode("p", text_to_children(clean_block)))

            case BlockType.CODE:
                text_node = TextNode(block[4:-3],TextType.PLAIN)
                children.append(ParentNode("pre",[ParentNode("code",[text_node_to_html_node(text_node)])]))
            
            case BlockType.QUOTE:
                lines = block.split('\n')
                clean_block = []
                for line in lines:
                    if(line.startswith('> ')):
                        clean_block.append(line[2:])
                    else:
                        clean_block.append(line[1:])
                clean_lines = ' '.join(l for l in clean_block)
                children.append(ParentNode("blockquote",text_to_children(clean_lines)))
            
            case BlockType.ORDERED_LIST:
                children.append(ParentNode("ol",block_to_line_items(block)))

            case BlockType.UNORDERED_LIST:
                children.append(ParentNode("ul",block_to_line_items(block)))

    parent_node = ParentNode('div',children)

    return parent_node    

def block_to_line_items(block: str) -> list[HTMLNode]:
    lines = block.split('\n')
    line_items = []
    i = 0
    for line in lines:
        i += 1
        if line.startswith("-"):
            line_items.append(ParentNode("li",text_to_children(line[2:])))
        else:
            prefix_length = len(f"{i}. ")
            line_items.append(ParentNode("li",text_to_children(line[prefix_length:])))
            
    return line_items

def text_to_children(block: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_blocks(markdown: str) -> list[str]:
    return list(filter(None,map(str.strip,markdown.split('\n\n'))))


def block_to_block_type(block: str) -> BlockType:
    split_block = block.split('\n')

    if block.startswith(('#','##','###','####','#####','######')):
        return BlockType.HEADING
    
    elif block.startswith('```\n') and block.endswith('```') and len(block)  > 6:
        return BlockType.CODE
    
    elif block.startswith('>'):
        for l in split_block:
            if not l.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    elif block.startswith('- '):
        for l in split_block:
            if not l.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    elif block.startswith('1. '):
        i = 1
        for l in split_block:
            if not l.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i+=1
        return BlockType.ORDERED_LIST
            
    else:
        return BlockType.PARAGRAPH
        

    