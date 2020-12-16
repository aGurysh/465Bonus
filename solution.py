


class GraphStruct():
    def __init__(self, graph):
        self.graph = graph

    def path_exists(self, fromV, toV, parent):
        pass

    def fulkerson(self, source, sink):
        pass






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

        #im rewriting the given graph to be 0-indexed
        # desired path will be from  edge #0 ->  edge #(nEdges -1)

        graph[fromV-1][toV-1] = capacity

    for line in graph:
        print(line)

    #initilize obj
    flowGraph = GraphStruct(graph)

    






if __name__ == "__main__":
    main()

