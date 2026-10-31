from .Map import Map

class ModelTemplate:

    def __init__(self,Map:Map):
        self.visited_nodes = []
        self.node_list = []
        self.Map=Map

    def next_node(self, node):
        return None

    def explore(self):
        pass