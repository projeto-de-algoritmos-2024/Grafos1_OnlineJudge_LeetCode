class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        mousePosition = 1
        catPosition = 2
        holePosition = 0
        
        #mouse turn
        #acha o caminho mais curto
        #vai pro seu vizinho na direcao do caminho mais curto
        mouseVisited = []
        
    def bfs (graph, visited, startPosition, AimedPosition):
        fila.append(startPosition)
        visited.append(startPosition)
        
        while fila:
            u = fila.pop(0)
            for each vizinho in graph[u]:
                if vizinho is not in visited:
                    
        