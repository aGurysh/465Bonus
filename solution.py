
'''
# Adam Gurysh amg6802
# Josephine Prickett jap6391
# Krish Parikh kap6006
# Kyle Ostrowski kto5055


CMPSC 465 Bonus problem 
MAX FLOW ACROSS NETWORK
(first given vertex will be source, last will be sink)

NOTE: The input data contains verticies named 1 through n, however, 
      the main function of this program generates an equivalent graph with verticies named 0 through n-1. 

    Thus the source vertex for the graph is (0) and the sink is (n-1)       

'''
class GraphStruct():
    def __init__(self, graph):
        self.graph = graph
        self.size = len(graph)

'''
                    Function: path_exists
        BFS based function to determine the existance of a path 
        between two verticies

        INPUT: starting vertex, ending vertex, parent list

        RETURNS: True if path exists, False if path doesnt exist
'''

    def path_exists(self, fromV, toV, parent):
        visited = [False] * self.size
        queue = []
        queue.append(fromV)
        visited[fromV] = True
        while queue:
            curV = queue.pop(0)
            #look at each edge from our current vertex
            for newV , capacity in enumerate(self.graph[curV]):
                #check that the edge exists and has not been visited
                if capacity > 0 and not visited[newV]:
                    #add new vertex to queue, mark visited, set parent
                    queue.append(newV)
                    visited[newV] = True
                    parent[newV] = curV   

        # were we able to successfully visit toV?
        return visited[toV]


'''
                    Function: fulkerson
        implementation of Ford-Fulkerson algorithm

        INPUT: source vertex, sink vertex

        RETURNS: True if path exists, False if path doesnt exist
'''

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

        #rewriting the given graph to be 0-indexed
        # desired path will be from  edge #0 ->  edge #(nEdges -1)
        graph[fromV-1][toV-1] = capacity

   

    #initilize obj
    flowGraph = GraphStruct(graph)





if __name__ == "__main__":
    main()

