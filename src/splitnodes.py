from textnode import TextNode, TextType
from enum import Enum
import re


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.PLAIN):
            new_nodes.append(node)
            continue
        
        split_str = node.text.split(delimiter)

        if len(split_str) % 2 == 0:
            raise Exception("Invalid Markdown syntax")

        split_nodes = []
        for i in range(len(split_str)):
            if split_str[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_str[i],TextType.PLAIN))
            else:
                split_nodes.append(TextNode(split_str[i],text_type))
        
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str,str]]:

    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def extract_markdown_links(text: str) -> list[tuple[str,str]]:

    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.PLAIN):
            new_nodes.append(node)
            continue

        extracted_images = extract_markdown_images(node.text)
        if (len(extracted_images) == 0):
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for i in extracted_images:
            split_node = remaining_text.split(f"![{i[0]}]({i[1]})", 1)
            if (split_node[0]):
                new_nodes.append(TextNode(split_node[0],TextType.PLAIN))
            new_nodes.append(TextNode(i[0],TextType.IMAGE,i[1]))
            remaining_text = split_node[1]
        if (remaining_text):
            new_nodes.append(TextNode(remaining_text,TextType.PLAIN))
        
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.PLAIN):
            new_nodes.append(node)
            continue

        extracted_links = extract_markdown_links(node.text)
        if (len(extracted_links) == 0):
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for i in extracted_links:
            split_node = remaining_text.split(f"[{i[0]}]({i[1]})", 1)
            if (split_node[0]):
                new_nodes.append(TextNode(split_node[0],TextType.PLAIN))
            new_nodes.append(TextNode(i[0],TextType.LINK,i[1]))
            remaining_text = split_node[1]
        if (remaining_text):
            new_nodes.append(TextNode(remaining_text,TextType.PLAIN))
        
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    text_nodes = [TextNode(text,TextType.PLAIN)]

    text_nodes = split_nodes_delimiter(text_nodes,'**',TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes,'_',TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes,'`',TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes                  