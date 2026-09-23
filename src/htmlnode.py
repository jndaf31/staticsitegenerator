
class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list['HTMLNode'] | None = None, props: dict[str,str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ''
        if self.props != None:
            for i in self.props.items():
                result += i[0] + '="' + i[1] + '" '
        return result[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if (isinstance(other, HTMLNode)
            and self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props):
                return True
        return False

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
        self.children = None

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
