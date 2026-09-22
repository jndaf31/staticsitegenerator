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
    


if __name__ == "__main__":
    unittest.main()