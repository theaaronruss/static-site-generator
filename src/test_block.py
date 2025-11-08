import unittest

from block import block_to_block_type
from block import BlockType

class TestBlock(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        markdown = "# This is a heading"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        markdown = "```This is a code block```"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        markdown = "> This is a quote"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        markdown = "- This is an unordered list"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        markdown = "1. This is an ordered list"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        markdown = "This is a paragraph"
        t = block_to_block_type(markdown)
        self.assertEqual(t, BlockType.PARAGRAPH)
