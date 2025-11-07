from textnode import TextType
from textnode import TextNode

def main():
    return TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

if __name__ == "__main__":
    print(main())
