import unittest

from inline_markdown import (
    split_nodes_delimiter,
)
from textnode import TextNode, TextType

class Test_inline_markdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_italic(self):
        node = TextNode("This is text with a **bolded word** and an _italic word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic word", TextType.ITALIC),
                ],
                new_nodes,
        )

    def test_delim_double_bold(self):
        node = TextNode("This **bold sentence** has three **bolded** words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual([
            TextNode("This ", TextType.TEXT),
            TextNode("bold sentence", TextType.BOLD),
            TextNode(" has three ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" words", TextType.TEXT),
        ],
        new_nodes
        )
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ],
        new_nodes,
        )

if __name__ == "__main__":
    unittest.main()