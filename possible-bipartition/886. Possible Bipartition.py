class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]  # Criando um grafo vazio
            
        for dislike in dislikes: # Construindo o grafo
            a, b = dislike
            graph[a].append(b)
            graph[b].append(a)
                
        colors = [0] * (n + 1)  # 0: sem cor, 1: verde, 2: amarelo

        for i in range(1, n + 1):
            if colors[i] == 0:  # node sem cor
                fila = [i]
                colors[i] = 1  # bota verde 

                while fila:
                    node = fila.pop(0)
                    corAtual = colors[node]

                    for vizinho in graph[node]:
                        if colors[vizinho] == 0:  # vizinho sem cor
                            colors[vizinho] = (-1) * corAtual  # bota cor oposta
                            fila.append(vizinho)
                        elif colors[vizinho] == corAtual:  # achou a mesma cor
                            return False

        return True