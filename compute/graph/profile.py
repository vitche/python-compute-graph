class ProfileGraph(Graph):
    def add(self, node):
        node = super().add(node)
        node.add(ProfilerNode())
        return node

class ProfilerNode(Node):
    def write(self, data):
        if None != data:
            self.arguments(data)
