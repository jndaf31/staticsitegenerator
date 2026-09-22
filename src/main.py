from textnode import *
from htmlnode import *

def main():
    obj = TextNode("Text Text",TextType.BOLD, "url")
    print(obj)

    htobj = HTMLNode("has","ewjfbekj", None, {"href": "https://www.google.com","target": "_blank",})
    print(htobj.props_to_html())
    print(htobj)
main()