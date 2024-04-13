class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        layers = [0] * (n+1) #groups
        fila = []
        visited = []
        
        for i in range(1, n+1):
            
            if layers[i] == 0: #usando o vetor pra saber 
                               # quais já foram visitados tb
                fila = [i]
                layers[i] = 1
                
                while fila:
                    noAtual = fila.pop(0)
                    layerAtual = layers[noAtual]
                    
                    for vizinho in dislikes[noAtual - 1]:
                        if (layers[noAtual] == 0):
                            layers[vizinho] = -1 * layerAtual
                            fila.append(vizinho)
                            
                        elif(layers[vizinho] == layerAtual):
                            return False
        
        return True
        