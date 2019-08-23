from compute.graph.structure import Graph
from compute.graph.structure import Node
from compute.graph.structure import Synapse

class ProfileGraph(Graph):
    def add(self, node):
        node = super().add(node)
        node.add(Synapse().add(ProfileNode()))
        return node

class ProfileNode(Node):
    def write(self, data):
        if None != data:
            self.arguments(data)
