from enum import Enum
from htmlnode import ParentNode, HTMLNode, LeafNode

def markdown_to_html_node(markdown: str)

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

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
        

    