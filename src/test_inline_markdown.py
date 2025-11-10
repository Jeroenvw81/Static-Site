import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_links,
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

    def test_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/image.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/image.png")], matches
        )

    def test_extract_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and a [second link](https://https://github.com/Jeroenvw81/Static-Site)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("second link", "https://https://github.com/Jeroenvw81/Static-Site"),
                ],
                matches,
        )
    
    def test_extract_markdown_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/image.png) and another ![second image](https://i.imgur.com/other_image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/image.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/other_image.png"),
            ],
            new_nodes,
        )

    def test_extract_markdown_links(self):
        node = TextNode(
            "This is text with a link to [youtube](https://www.youtube.com)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://www.youtube.com")
            ],
            new_nodes
        )

    def test_extract_markdown_three_links(self):
        node = TextNode(
            "This is text with links to [youtube](https://youtube.com), [bootdev](https://boot.dev) and a third link to [google](https://google.com)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with links to ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://youtube.com"),
                TextNode(", ", TextType.TEXT),
                TextNode("bootdev", TextType.LINK, "https://boot.dev"),
                TextNode(" and a third link to ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com")
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()