import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("a", "link", [HTMLNode(), HTMLNode()], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("a", "link", [HTMLNode(), HTMLNode()], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(' href="https://www.boot.dev" target="_blank"', node.props_to_html())

    def test_props_to_html_empty(self):
        node = HTMLNode("a", "link", [HTMLNode(), HTMLNode()], {})
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_none(self):
        node = HTMLNode("a", "link", [HTMLNode(), HTMLNode()], {})
        self.assertEqual("", node.props_to_html())
