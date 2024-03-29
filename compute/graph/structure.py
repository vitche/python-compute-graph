from compute.graph.activation import Activation


class Graph:

    def __init__(self):
        self.nodes = []
        self.firstNode = None
        self.previousNode = None        

    def add(self, node):

        if self.firstNode is None:
            self.firstNode = node

        if self.previousNode is not None:
            self.previousNode.add(Synapse().add(node))

        self.previousNode = node
        self.nodes.append(node)
        return node

    def attach(self, node):
        self.nodes.append(node)
        return node

    def connect(self, subgraph):
        self.add(subgraph.first())

    def first(self):
        return self.firstNode

    def fork(self, node):
        subgraph = self.__class__()
        subgraph.add(node)
        activation_node = SubgraphActivationNode(subgraph)
        self.previous().add(Synapse().add(activation_node))
        self.attach(activation_node)
        return subgraph

    def previous(self):
        return self.previousNode

    def write(self, data):
        self.firstNode.write(data)


class Node:

    def __init__(self):
        self.__arguments = []
        self.__synapses = []

    def add(self, synapse):
        self.__synapses.append(synapse)
        return self

    def arguments(self, value):
        self.__arguments = value

    def read(self):
        result = self.__arguments
        self.__arguments = []
        return result

    def write(self, data):
        if data is not None:
            self.__arguments += data

    def initialize(self):
        return

    def activate(self):
        self.process()
        data = self.read()
        if data is not None:
            for i in range(len(self.__synapses)):
                synapse = self.__synapses[i]
                synapse.write(data)
    
    def process(self):
        return
    
    def synapses(self):
        return self.__synapses


class SpreadNode(Node):
    def process(self):
        data = self.read()
        synapses = self.synapses()
        for synapse in synapses:
            for item in data:
                synapse.write([item])
                synapse.node().activate()


class SubgraphActivationNode(Node):
    def __init__(self, subgraph):
        super().__init__()
        self.subgraph = subgraph
        self.add(Synapse().add(subgraph.first()))

    def process(self):
        data = self.read()
        self.subgraph.first().write(data)
        Activation().iterate(self.subgraph.nodes)


class Synapse:

    __node: None

    def add(self, node):
        self.__node = node
        return self

    def node(self):
        return self.__node
    
    def write(self, data):
        self.__node.write(data)
