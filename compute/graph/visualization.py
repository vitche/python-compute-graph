from graphviz import Digraph
from graphviz import Source

import graphviz
from IPython.display import display

from compute.graph.structure import Node
from compute.graph.profile import ProfileNode

class GraphvizNode(Node):

    def __traverse(self, graph, node):

        synapses = node.synapses()

        # Extract deltas from profiler nodes if any
        delta = None
        for i in range(len(synapses)):
            neighborNode = synapses[i].node()
            if isinstance(neighborNode, ProfileNode):
                deltas = neighborNode.read()
                if 0 < len(deltas):
                    delta = deltas[0]

        for i in range(len(synapses)):
            neighborNode = synapses[i].node()
            if isinstance(neighborNode, ProfileNode):
                continue
            graph.node(str(neighborNode))
            self.__traverse(graph, neighborNode)
            label = ""
            if None != delta:
                amountDeltaString = str(delta["amount"])
                if 0 < delta["amount"]:
                    amountDeltaString = "+" + amountDeltaString
                label = amountDeltaString + " (N), " + str(delta["time"]) + " (s)"
            graph.edge(str(node), str(neighborNode), label = label)

    def process(self):
        dot = Digraph()
        self.__traverse(dot, self)
        display(Source(dot))
