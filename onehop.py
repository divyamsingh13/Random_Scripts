#program to check if user can reach a nod of graph using only one hop from start
from collections import defaultdict



class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isReachable(self, s, d):
        a=self.graph[s]
        for i in a:
            b=self.graph[i]
            if(d in b):
                return True
        return False


# Create a graph given in the above diagram
    def onehop(a):
        g=Graph(len(a))
        b=list()
        for i in a:

            g.addEdge(i[0],i[1])
        for i in g.graph:

            for j in g.graph:

                if(i!=j and g.isReachable(i,j)):

                    b.append((i,j))
        print(b)

Graph.onehop([(2,3),(1,2)])
