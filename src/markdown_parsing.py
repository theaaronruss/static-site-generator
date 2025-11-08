import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None or len(old_nodes) == 0:
        return []
    new_nodes = []
    for old_node in old_nodes:
        parts = old_node.text.split(delimiter)

        if len(parts) % 2 != 1:
            raise ValueError("invalid markdown syntax")

        for i in range(0, len(parts)):
            node = None
            if i % 2 == 0:
                node = TextNode(parts[i], TextType.PLAIN)
            else:
                node = TextNode(parts[i], text_type)
            new_nodes.append(node)
    return new_nodes

def extract_markdown_links(text):
    if text is None:
        return []
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    if text is None:
        return []
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
