
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
        