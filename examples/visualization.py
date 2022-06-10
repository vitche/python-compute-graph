from compute.graph.structure import Node
from compute.graph.profile import ProfileGraph
from compute.graph.visualization import GraphvizNode

graph = ProfileGraph()
graph.add(GraphvizNode())
graph.add(Node())
graph.add(Node())
graph.add(Node())
graph.add(Node())
graph.add(Node())
graph.add(Node())
graph.add(Node())

graph.first().activate()

print(graph)
