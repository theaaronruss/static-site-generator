import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("First text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Second text node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("Text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Text node", TextType.IMAGE, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("Text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("Text node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://www.boot.dev/img.png")
        self.assertEqual(html_node.props["alt"], "This is an image node")

    def test_text_node_to_html_node_unknown(self):
        node = TextNode("This is an unknown node", "unknown")
        self.assertRaises(ValueError, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()
