from collections import deque, defaultdict
from typing import List

class Solution:
                    
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        #Posicoes iniciais
        # mouse = 1
        # cat = 2
        # hole= 0
        
        #como ganha? Quais sao os states possiveis?
        #rato no 0 = ratou ganhou -> retorna 1
        #gato no msm lugar que o rato = gato ganhou -> retorna 2
        #empate - Gato e rato tão repetindo posicao -> retorna 0
        
        # É um algoritmo que trabalha de trás pra frente. Então ele
        # vai das posiç~oes ganhadoras finais e andando até o começo
        # nas posicoes iniciais. Enquanto ele anda ele vai marcando 
        # pra cada combinacao de posicao do rato, do gato e o turno 
        # quem ganha naquele estado. Dai, quando ele percorreu todas 
        # as possibilidades possiveis, ele so retorna qual vai ser 
        # o resultado para o estado inicial
        
        numNodes = len(graph)
        fila = deque()
        stateResults = defaultdict(int)
        
        #Estados finais desejados(mousePosition, catPosition, turno(1 rato, 2 gato) = quem tá ganhando nesse state)
        for turn in [1,2]:
            for node in range(numNodes):
                #estado final vitoria do rato
                stateResults[(0,node, turn)] = 1
                fila.append((0, node, turn))
                
                #estado final vitoria do gato
                stateResults[(node, node, turn)] = 2
                fila.append((node, node, turn))
                
        #Próximo estado- contar arestas de saidas,
        # quantos estados possíveis a partir desse estado
        numProxStatesPossiveis = [[[0]*numNodes for mouse in range(numNodes)] for turn in range(3)]
        # matriz tridimensional de numNode x numNodes x 3
        
        for turn in range(1, 3):
            for mouse in range(numNodes):
                for cat in range(numNodes):
                    if turn == 1: #vez do rato
                        numProxStatesPossiveis[turn][mouse][cat] = len(graph[mouse])
                    else: #vez do gato, gato é proibido de passar no node 0
                        numProxStatesPossiveis[turn][mouse][cat] = len(graph[cat]) - (0 in graph[cat])
                        
        #Pegar o estado anterior a partir do atual
        def getStateAnterior (mouse, cat, turn):
            statesAnteriores = []
            for node in graph[mouse if turn == 2 else cat]:
                if turn == 1 and node == 0:
                    #vez do rato, ele alcança o buraco 0 na proxima
                    continue 
                if turn == 1:
                    #vez do rato, logo o estado anterior é
                    #onde o rato tá agora, onde o gato tava antes, e o turno do gato
                    statesAnteriores.append((mouse, node, 2))
                if turn == 2:
                    #vez do gato, logo o estado anterior é
                    #onde o rato tava antes, onde o gato ta agora e o turno do rato
                    statesAnteriores.append((node, cat, 1))
                    
            return statesAnteriores
                
        #BFS
        while fila:
            mouse, cat, turn = fila.popleft() #proximo state, que a gnt ja sabe pq tamo indo de tras pra frente
            result = stateResults[(mouse,cat,turn)]
            for mouseAnt, catAnt, turnAnt in getStateAnterior(mouse, cat, turn):
                #state anterior que queremos calcular
                
                if (mouseAnt, catAnt, turnAnt) in stateResults:
                    continue #ja calculou? passa reto
                if result == turnAnt:
                    stateResults[(mouseAnt, catAnt, turnAnt)] = result
                    fila.append((mouseAnt, catAnt, turnAnt))
                else:
                    numProxStatesPossiveis[turnAnt][mouseAnt][catAnt] -=1
                    if numProxStatesPossiveis[turnAnt][mouseAnt][catAnt] == 0:
                        stateResults[(mouseAnt, catAnt, turnAnt)] = 3 - turnAnt #ex: gato turn 2: 3-2 = 1 rato ganhou
                        fila.append((mouseAnt, catAnt, turnAnt))
                        
        return stateResults[(1, 2, 1)]  