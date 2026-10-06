from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN = 'plain'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'img'

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (isinstance(other, TextNode)
            and self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node:TextNode) -> LeafNode:
        match text_node.text_type:
            case TextType.PLAIN:
                return LeafNode(None,text_node.text)
            case TextType.BOLD:
                return LeafNode('b',text_node.text)
            case TextType.ITALIC:
                return LeafNode('i',text_node.text)
            case TextType.CODE:
                return LeafNode('code', text_node.text)
            case TextType.LINK:
                if isinstance(text_node.url,str):
                    return LeafNode('a', text_node.text, {'href': text_node.url})
                else: 
                    raise ValueError("Invalid URL")
            case TextType.IMAGE:
                if isinstance(text_node.url, str):
                    return LeafNode('img','',{'src':text_node.url,'alt':text_node.text})
                else: 
                    raise ValueError("Invalid URL")
            case _:
                raise ValueError("Invalid Type")