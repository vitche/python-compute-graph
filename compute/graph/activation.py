class Activation:
    
    def iterate(self, nodes):
        for i in range(len(nodes)):
            node = nodes[i]
            node.activate()
