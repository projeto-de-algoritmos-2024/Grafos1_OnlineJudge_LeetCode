def bfs (graph, startPosition, aimedPosition, visited):
    fila = [startPosition]
    looked = {startPosition}
    
    while fila:
        noAtual = fila.pop(0)
        if noAtual == aimedPosition:
            return looked
        
        for vizinho in graph[noAtual]:
            if (vizinho not in visited) and (vizinho not in looked):
                looked.add(vizinho)
                fila.append(vizinho)
    return None
class Solution:
                    
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        mousePosition = 1
        catPosition = 2
        holePosition = 0

        mouseVisited = set()
        catVisited = set()
        catVisited.add(holePosition)
        
        result = -1
        
        while (result == -1):
            
            mouseLooked = bfs(graph,mousePosition, holePosition, mouseVisited)
            
            if mouseLooked:
                result = 1
            else:
                catLooked = bfs(graph,catPosition, mousePosition, catVisited)
                if catLooked & mouseLooked:
                    result = 2
                else:
                    mouseVisited.update(mouseLooked or set([mousePosition]))
                    catVisitedx.update(catLooked or set([catPosition]))
                    
                    if mousePosition in mouseVisited and mouseLooked is None:
                        result = 0
                    elif catPosition in catVisited and catLooked is None:
                        result = 0
                        
                    mousePosition = (catPosition if result != 2 else mousePosition)
                    
        return result
        

                    
        