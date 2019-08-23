from compute.graph.structure import Graph
from compute.graph.structure import Node

class ProfileGraph(Graph):
    def add(self, node):
        node = super().add(node)
        node.add(ProfilerNode())
        return node

class ProfileNode(Node):
    def write(self, data):
        if None != data:
            self.arguments(data)
