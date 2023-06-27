class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def add_edge(self, node1, node2):
        # Undirected Graph
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def show_connections(self):
        all_nodes = list(self.adjacentList.keys())
        for node in all_nodes:
            node_connections = self.adjacentList[node]
            connections = " ".join(node_connections)
            print(node + "-->" + connections)


myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')

myGraph.show_connections()
# Answer:
# 0-->1 2
# 1-->3 2 0
# 2-->4 1 0
# 3-->1 4
# 4-->3 2 5
# 5-->4 6
# 6-->5
