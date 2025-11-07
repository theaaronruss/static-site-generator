import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_raw_value(self):
        node = LeafNode(None, "The value", None)
        self.assertEqual("The value", node.to_html())

    def test_to_html_no_value(self):
        node = LeafNode("a", None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html(self):
        node = LeafNode("a", "click", {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual('<a href="https://www.boot.dev" target="_blank">click</a>', node.to_html())

    def test_to_html_no_props(self):
        node = LeafNode("a", "click", None)
        self.assertEqual("<a>click</a>", node.to_html())
        
    def test_to_html_empty_props(self):
        node = LeafNode("a", "click", {})
        self.assertEqual("<a>click</a>", node.to_html())
