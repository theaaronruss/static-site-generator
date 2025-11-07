import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span>child</span></div>", parent_node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span><b>grandchild</b></span></div>", parent_node.to_html())

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_empty_children(self):
        node = ParentNode(None, [])
        self.assertRaises(ValueError, node.to_html)
