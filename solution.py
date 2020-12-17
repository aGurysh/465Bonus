
'''
# Adam Gurysh amg6802
# Josephine Prickett jap6391
# Krish Parikh kap6006
# Kyle Ostrowski kto5055

'''
'''
 ________                         __          ________          __  __                                                         
/        |                       /  |        /        |        /  |/  |                                                        
$$$$$$$$/______    ______    ____$$ |        $$$$$$$$/__    __ $$ |$$ |   __   ______    ______    _______   ______   _______  
$$ |__  /      \  /      \  /    $$ | ______ $$ |__  /  |  /  |$$ |$$ |  /  | /      \  /      \  /       | /      \ /       \ 
$$    |/$$$$$$  |/$$$$$$  |/$$$$$$$ |/      |$$    | $$ |  $$ |$$ |$$ |_/$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$/ /$$$$$$  |$$$$$$$  |
$$$$$/ $$ |  $$ |$$ |  $$/ $$ |  $$ |$$$$$$/ $$$$$/  $$ |  $$ |$$ |$$   $$<  $$    $$ |$$ |  $$/ $$      \ $$ |  $$ |$$ |  $$ |
$$ |   $$ \__$$ |$$ |      $$ \__$$ |        $$ |    $$ \__$$ |$$ |$$$$$$  \ $$$$$$$$/ $$ |       $$$$$$  |$$ \__$$ |$$ |  $$ |
$$ |   $$    $$/ $$ |      $$    $$ |        $$ |    $$    $$/ $$ |$$ | $$  |$$       |$$ |      /     $$/ $$    $$/ $$ |  $$ |
$$/     $$$$$$/  $$/        $$$$$$$/         $$/      $$$$$$/  $$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/   $$$$$$/  $$/   $$/ 
'''
class GraphStruct():
    def __init__(self, graph):
        self.graph = graph
        self.size = len(graph)

    '''
                    Function: fulkerson
        implementation of Ford-Fulkerson algorithm

        INPUT: source vertex, sink vertex

        RETURNS: True if path exists, False if path doesnt exist
    '''

    def fulkerson(self, source, sink):
        #set up parent list, define var for result
        parent = [-1] * self.size
        maximumFlow = 0

        #loop until no path from source to sink
        while self.ford(source, sink, parent):
            thisPathFlow = float("Inf")
            tempV = sink

            #the max flow on this path is equal to the smallest edge capacity it contains
            while(tempV != source):
                #reduce thisPathFlow if neccesary
                thisPathFlow = min(thisPathFlow, self.graph[parent[tempV]][tempV])
                #move tempV towards source
                tempV = parent[tempV]

            #add the max flow for this path to the total
            maximumFlow = maximumFlow +  thisPathFlow

            #now update residual values in graph
            
            tempV2 = sink
            while(tempV2 != source):
                p = parent[tempV2]
                self.graph[p][tempV2] = self.graph[p][tempV2] - thisPathFlow
                self.graph[tempV2][p] = self.graph[tempV2][p] + thisPathFlow
                tempV2 = parent[tempV2]
       
        return maximumFlow
    
    '''
                    Function: ford
        BFS based function to determine the existance of a path 
        between two verticies

        INPUT: starting vertex, ending vertex, parent list

        RETURNS: True if path exists, False if path doesnt exist
    '''

    def ford(self, fromV, toV, parent):
        visited = [False] * self.size
        queue = []
        queue.append(fromV)
        visited[fromV] = True
        while queue:
            curV = queue.pop(0)
            #look at each edge from our current vertex
            for i in range(len(self.graph[curV])):
                capacity = self.graph[curV][i]
                newV = i
                #check that the edge exists and has not been visited
                if capacity > 0 and not visited[newV]:
                    #add new vertex to queue, mark visited, set parent
                    queue.append(newV)
                    visited[newV] = True
                    parent[newV] = curV   

        # were we able to successfully visit toV?
        return visited[toV]



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
        graph[fromV-1][toV-1] += capacity
   
    #initilize obj
    flowGraph = GraphStruct(graph)
    print(flowGraph.fulkerson(0,nVerticies-1))

    
if __name__ == "__main__":
    main()
