class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        layer = 0 #groups par ou impar
        fila = []
        visited = []
        
        for i in dislikes:
            if i not in visited:
                fila.append(i)
                fila.append(layer)
                while fila:
                    noAtual = fila.pop(0)
                    layerAtual = fila.pop(0)
                    visited.append(noAtual)
                    
                    for vizinho in dislikes[noAtual]:
                        if (vizinho not in visited):
                            visited.append(vizinho)
                            fila.append(vizinho)
                            fila.append(layerAtual + 1)
                        elif( noAtual == fila[vizinho + 1]):
                            return false
        
        return true
        