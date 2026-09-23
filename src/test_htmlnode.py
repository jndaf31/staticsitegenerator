import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Valuess", None, {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("p", "Valuess", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("p", "Valuess", None, {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("p", None, [node], {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_eq_tohtml(self):
        node = HTMLNode("p", "Valuess", None, {"href": "https://www.google.com","target": "_blank",}).props_to_html()
        node2 = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')


if __name__ == "__main__":
    unittest.main()