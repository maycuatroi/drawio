import typing

if typing.TYPE_CHECKING:
    from .node import Node


class Edge:
    def __init__(self, parent: "Node", child: typing.Union["Node", None], label=None):

        self.label = label
        self.parent = parent
        self.child = child

    def __rshift__(self, other: typing.Union["Node"]):
        """
        If is node, create new edge and add child node
        """
        self.child = other
        self.child.add_parent_edge(self)
        return self.child

    def __repr__(self):
        if self.label:
            return f"{self.parent.name}--{self.label}-->{self.child.name}"
        else:
            return f"{self.parent.name}-->{self.child.name}"

    def __eq__(self, other):

        child_name = self.child.name if self.child else None
        other_child_name = other.child.name if other.child else None
        parent_name = self.parent.name if self.parent else None
        other_parent_name = other.parent.name if other.parent else None
        label = self.label if self.label else None
        return (
            child_name == other_child_name
            and parent_name == other_parent_name
            and label == other.label
        )
