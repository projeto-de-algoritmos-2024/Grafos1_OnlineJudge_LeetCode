def bfs (graph, startPosition, AimedPosition, visited):
    fila = [startPosition]
    looked = [startPosition]
    
    while fila:
        u = fila.pop(0)
        if u == AimedPosition:
            return looked[1]
        
        for vizinho in graph[u]:
            if (vizinho not in visited) and (vizinho not in looked):
                looked.append(vizinho)
                fila.append(vizinho)
class Solution:
                    
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        mousePosition = 1
        catPosition = 2
        holePosition = 0

        mouseVisited = []
        catVisited = []
        catVisited.append(holePosition)
        
        result = -1
        
        while (result == -1):
            
            mousePosition = bfs(graph,mousePosition, holePosition, mouseVisited)
            catPosition = bfs(graph,catPosition, mousePosition, catVisited)
            
            mouseVisited.append(mousePosition)
            catVisited.append(catPosition)
            
            if mousePosition == holePosition:
                result = 1
            elif mousePosition == catPosition:
                result = 2
            elif (len(graph) == len(mouseVisited)) or (len(graph) == len(catVisited)):
                result = 0
            
        return result
        

                    
        