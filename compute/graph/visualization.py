from graphviz import Digraph
# from graphviz import Source
# import graphviz
# from IPython.display import display

from compute.graph.structure import Node
from compute.graph.profile import ProfileNode


class GraphvizNode(Node):
    __opened = []

    def __traverse(self, graph, node):

        # Do not traverse the node twice
        if node in self.__opened:
            return
        self.__opened.append(node)

        synapses = node.synapses()

        # Extract deltas from profiler nodes if any
        delta = None
        for i in range(len(synapses)):
            neighbor_node = synapses[i].node()
            if isinstance(neighbor_node, ProfileNode):
                deltas = neighbor_node.read()
                if 0 < len(deltas):
                    delta = deltas[0]

        for i in range(len(synapses)):
            neighbor_node = synapses[i].node()
            if isinstance(neighbor_node, ProfileNode):
                continue
            graph.node(str(neighbor_node))
            self.__traverse(graph, neighbor_node)
            label = ""
            if delta is not None:
                amount_delta_string = str(delta["amount"])
                if 0 < delta["amount"]:
                    amount_delta_string = "+" + amount_delta_string
                label = amount_delta_string + " (N), " + str(delta["time"]) + " (s)"
            graph.edge(str(node), str(neighbor_node), label=label)

    def process(self):

        dot = Digraph()
        self.__opened = []
        self.__traverse(dot, self)
        dot.format = 'png'
        dot.render(str(self))

        # The rendered graph is usually huge. 
        # So, immediate displaying was disabled.
        # display(Source(dot))
