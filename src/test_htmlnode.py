import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="link",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        props_str = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', props_str)
        self.assertIn(' target="_blank"', props_str)

    
    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="hello", props=None)
        self.assertEqual(node.props_to_html(), "")


    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="p", value="hi", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    
    def test_parent_node_single_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    
    def test_parentnode_with_grandchild(self):
        grandchild = LeafNode("b", "strong")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>strong</b></span></div>",
        )

    def test_parentnode_missing_tag_raises(self):
        child = LeafNode("span", "child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parentnode_missing_children_raises(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parentnode_multiple_children(self):
        child1 = LeafNode("b", "Bold")
        child2 = LeafNode(None, " plain ")
        child3 = LeafNode("i", "italic")
        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b> plain <i>italic</i></p>",
        )




if __name__ == "__main__":
    unittest.main()