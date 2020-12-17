# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow



def main():
    #extract graph information from first line of input
    graphData = [int(x) for x in input().split()]
    nVerticies = graphData[0]
    nEdges = graphData[1]

    #constructing graph as 2D array
    graph = [ [0]* (nVerticies) for i in range(nVerticies)]

    for _ in range(nEdges):
        edgeData = [int(x) for x in input().split()]
        fromV = edgeData[0]
        toV = edgeData[1]
        capacity = edgeData[2]

        #rewriting the given graph to be 0-indexed
        graph[fromV-1][toV-1] = capacity

        g = Graph(graph)


        source = 0
        sink = nVerticies -1
        print("Max Flow: %d " % g.ford_fulkerson(source, sink))