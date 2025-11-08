import unittest
from textnode import TextNode
from textnode import TextType
from markdown_parsing import split_nodes_delimiter
from markdown_parsing import extract_markdown_links
from markdown_parsing import extract_markdown_images

class TestSplitter(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "bold block")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "italic block")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_only_text(self):
        node = TextNode("This is text with no formatting", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is text with no formatting")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode("This is **text** with **multiple** bold blocks", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "text")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " with ")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[3].text, "multiple")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[4].text, " bold blocks")
        self.assertEqual(new_nodes[4].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_empty(self):
        new_nodes = split_nodes_delimiter([], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [])

    def test_split_nodes_delimiter_none(self):
        new_nodes = split_nodes_delimiter(None, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [])

    def test_split_nodes_delimiter_invalid(self):
        node = TextNode("This is text with a _italic block word", TextType.PLAIN)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "_", TextType.ITALIC)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_markdown_links_empty(self):
        text = ""
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_extract_markdown_links_none(self):
        links = extract_markdown_links(None)
        self.assertEqual(links, [])

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_images_empty(self):
        text = ""
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_none(self):
        images = extract_markdown_images(None)
        self.assertEqual(images, [])
