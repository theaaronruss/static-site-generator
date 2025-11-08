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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes

def extract_markdown_links(text):
    if text is None:
        return []
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    if text is None:
        return []
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
