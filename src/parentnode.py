from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("parent node must have children")
        
        value = ""
        for child in self.children:
            value += child.to_html()

        return f"<{self.tag}>{value}</{self.tag}>"
