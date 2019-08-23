from compute.graph.structure import Graph
from compute.graph.structure import Node
from compute.graph.structure import Synapse

class ProfileGraph(Graph):
    def add(self, node):
        node = super().add(node)
        node.add(Synapse().add(ProfileNode()))
        return node

class ProfileNode(Node):
    def __init__(self):
        super().__init__()
        self.delta = {
            "amount": 0,
            "time": 0
        }
    def write(self, data):
        if None != data:
            for item in data:
                if isinstance(item, dict):
                    if 'amount' in item and 'time' in item:
                        self.delta["amount"] += item["amount"]
                        self.delta["time"] += item["time"]
        self.arguments([self.delta])
