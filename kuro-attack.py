class Node:
    def __init__(self, num):
        self.num = num
        self.vizinhos = []
    
    def add_vizinho (self, vizinho):
        jaSaoVizinhos = False
        for i in self.vizinhos:
            if i == vizinho:
                jaSaoVizinhos = True
                break
        if jaSaoVizinhos == False:
            self.vizinhos.append(vizinho)
            vizinho.vizinhos.append(self)

def main():
    graphServers = []
    
    firstLine = input()
    maxServer = int(firstLine[0])
    kuroNumber = int(firstLine[2])
    
    line = input()
    startNode = existe(graphServers, int(line[0]))
    server2 = existe(graphServers, int(line[2]))
    startNode.add_vizinho(server2)
    
    for i in range(maxServer-2):
        line = input()
        server1 = existe(graphServers, int(line[0]))
        server2 = existe(graphServers, int(line[2]))
        server1.add_vizinho(server2)
    
    infected = bfs(startNode, kuroNumber)
    
    if (infected != -1):
        print(str(infected))
   
    if maxServer > infected:
        print("Impossible Revenge!")

def existe(grafo, num): #se existe mostra, se nao existe cria e devolve
    existe = 0
    for i in grafo:
        if i.num == num:
            existe = 1
            return i
    if existe == 0:
        node = Node(num)
        grafo.append(node)
        return node

def bfs (startNode, kuroNumber):
    fila = []
    fila.append(startNode)
    fila.append(0)
    infected = []
    infected.append(startNode)
    
    while (len(fila) > 0):
        server = fila.pop(0)
        distanceLayers = fila.pop(0)
        
        if distanceLayers == kuroNumber :
            return len(infected)
        
        for serverVizinho in server.vizinhos:

            if serverVizinho not in infected:
                fila.append(serverVizinho)
                fila.append(distanceLayers + 1)
                infected.append(serverVizinho)
    return -1
        
        
main() 
    