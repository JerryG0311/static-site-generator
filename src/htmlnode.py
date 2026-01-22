class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props



    def to_html(self):
        raise NotImplementedError
    

    
    def props_to_html(self):
        if not self.props:
            return ""
        props_string = ""
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        return props_string
    

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    

    def to_html(self):
        if self.tag == "img":
            return f"<img{self.props_to_html()} />"
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    
    def to_html(self):
        if not self.tag:
            raise ValueError("Object is missing a tag")
        if self.children is None:
            raise ValueError("No children were provided")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
      
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"