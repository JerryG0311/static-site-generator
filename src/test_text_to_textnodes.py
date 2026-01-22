import unittest
from functions import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_full_markdown_pipeline(self):
        text = (
            "This is **bold** and _italic_ and `code` "
            "and ![img](https://example.com/a.png) "
            "and [link](https://example.com)"
        )

        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://example.com/a.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]

        self.assertListEqual(nodes, expected)

    
    def test_plain_text(self):
        text = "just some normal text"
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("just some normal text", TextType.TEXT)
        ]
        
        self.assertListEqual(nodes, expected)

    
    def test_bold_only(self):
        text = "This is **bold**"
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        
        self.assertListEqual(nodes, expected)


    def test_starts_with_markdown(self):
        text = "**bold** text"
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        
        self.assertListEqual(nodes, expected)

    
    def test_unmatched_delimiter_raises(self):
        text = "this is **broken"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)


    def test_ends_with_markdown(self):
        text = "Text **bold**"
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]

        self.assertListEqual(nodes, expected)



if __name__ == "__main__":
    unittest.main()