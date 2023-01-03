import typing

from shortuuid import uuid

from drawio.entities import config
from drawio.entities.graph.edge import Edge


class Node:
    def __init__(self, name, shape="ellipse", color="#00000"):
        self.name = name
        self.id = uuid()
        self.children = []
        self.parents = []
        self.shape = shape
        self.color = color
        self.bg_color = "#ffffff".upper()
        self.graph = config.GLOBAL_GRAPH

    # overwrite >> function
    def __rshift__(self, other: typing.Union["Node", str]):
        """
        If is node, create new edge and add child
        If is string, save as label and return my self
        """
        if isinstance(other, Node):
            return self.add_child(other)
        elif isinstance(other, list):
            for node in other:
                self.add_child(node)
        elif isinstance(other, str):
            child_edge = Edge(parent=self, child=None, label=other)
            self.children.append(child_edge)
            self.graph.add_edge(child_edge)
            return child_edge

    def __sync_graph(self, other_node: "Node"):
        """
        If node 1 and node 2 have at least one graph not None, set the graph to the other node
        """
        if self.graph is not None:
            other_node.graph = self.graph
        elif other_node.graph is not None:
            self.graph = other_node.graph

    def add_child(self, child: "Node"):
        """
        Add child to node
        """
        child_edge = Edge(parent=self, child=child, label=None)

        if child_edge not in self.children:
            self.children.append(child_edge)
            child.add_parent(self)
            self.__sync_graph(child)
            self.graph.add_node(child)
            self.graph.add_edge(child_edge)
        return child_edge.child

    def add_parent(self, parent: "Node"):
        """
        Add parent to node
        """
        parent_edge = Edge(parent=parent, child=self, label=None)
        parent_edge = self.add_parent_edge(parent_edge)
        self.__sync_graph(parent)
        self.graph.add_edge(parent_edge)
        self.graph.add_node(parent)
        return parent_edge.parent

    def add_parent_edge(self, parent_edge: Edge):
        if parent_edge not in self.parents:
            self.parents.append(parent_edge)
        return parent_edge

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_neighbours(self):
        parent_nodes = [edge.parent for edge in self.parents]
        child_nodes = [edge.child for edge in self.children]
        return parent_nodes + child_nodes

    def get_edge(self, neighbour: "Node"):
        edges = self.parents + self.children
        for edge in edges:
            if edge.parent == neighbour or edge.child == neighbour:
                return edge

        return None

    def set_color(self, color, bg_color):
        self.color = color
        self.bg_color = bg_color
