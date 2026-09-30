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
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_mult_children(self):
        child_node = LeafNode("span", "child")
        child2_node = LeafNode("b", "child2")
        child3_node = LeafNode("i", "child3")
        parent_node = ParentNode("div", [child_node,child2_node,child3_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>child2</b><i>child3</i></div>")

    def test_to_html_link_children(self):
        child_node = LeafNode("span", "child",{"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span href="https://www.google.com">child</span></div>')


if __name__ == "__main__":
    unittest.main()