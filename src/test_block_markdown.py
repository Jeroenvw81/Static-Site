import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class test_block_markdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = "> quote\n>more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UOLIST)
        block = "1. item\n2. other item"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "just a paragraph of text, or is it?"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        