class Node:
    def __init__(self, num):
        self.num = num
        self.vizinhos = []
    
    def add_vizinho (self, vizinho):
        self.vizinhos.append(vizinho)
        vizinho.vizinhos.append(self)

def main():
    firstLine = input()
    maxServer = int(firstLine[0])
    kuroNumber = int(firstLine[2])
    
    line = input()
    line.split()
    
    startNode = Node(line[0])
    server2 = Node(line[2])
    
    startNode.add_vizinho(server2)
    
    for i in range(maxServer-2):
        Line = input()
        Line.split(" ")
        
        server1 = Node(firstLine[0])
        server2 = Node(firstLine[2])
        
        server1.add_vizinho(server2)

    infected = bfs(startNode, kuroNumber)
    
    print(str(infected))
    if maxServer > infected:
        print("Impossible Revenge!")
  

def bfs (startNode, kuroNumber):
    fila = []
    fila.append(startNode)
    fila.append(0)
    infected = [startNode]
    
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
    