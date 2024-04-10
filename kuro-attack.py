class Node:
    def __init__(self, num):
        self.num = num
        self.vizinhos = []
    
    def add_vizinho (self, vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)
            vizinho.vizinhos.append(self)

def main():
    while True:
        try:
            graphServers = []
            firstLine = input().split()
            maxServer = int(firstLine[0])
            kuroNumber = int(firstLine[1])
            
            for _ in range(maxServer - 1):
                line = input().split()
                server1 = existe(graphServers, int(line[0]))
                server2 = existe(graphServers, int(line[1]))
                server1.add_vizinho(server2)
            
            startNode = graphServers[0]
            infected = bfs(startNode, kuroNumber)
            
            if infected != -1:
                print(str(infected))
            else:
                print("Impossible Revenge!")
        except EOFError:
            break

def existe(grafo, num): #se existe mostra, se nao existe cria e devolve
    for i in grafo:
        if i.num == num:
            return i
    node = Node(num)
    grafo.append(node)
    return node

def bfs (startNode, kuroNumber):
    fila = []
    fila.append(startNode)
    fila.append(0)
    infected = set()
    infected.add(startNode)
    
    while fila:
        server = fila.pop(0)
        distanceLayers = fila.pop(0)
        
        if distanceLayers == kuroNumber:
            return len(infected)
        
        for serverVizinho in server.vizinhos:
            if serverVizinho not in infected:
                fila.append(serverVizinho)
                fila.append(distanceLayers + 1)
                infected.add(serverVizinho)
    return -1

main()
