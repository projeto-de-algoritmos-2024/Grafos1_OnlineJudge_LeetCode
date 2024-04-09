class Node:
    def __init__(self, num):
        self.num = num
        self.vizinhos = []
    
    def add_vizinho (self, vizinho):
        self.vizinhos.append(vizinho)

def main():
    maxServer = 9
    kuroNumber = 3
    
    startNode = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    
    startNode.add_vizinho(node2)
    node2.add_vizinho(node7)
    node2.add_vizinho(node3)
    node2.add_vizinho(node4)
    node4.add_vizinho(node5)
    node4.add_vizinho(node6)
    node4.add_vizinho(node8)
    node8.add_vizinho(node9)
    node5.add_vizinho(node3)
    
    
    infected = bfs(startNode, kuroNumber)
    
    print(str(infected))
    if maxServer > infected:
        print("Impossible Revenge!")
  

def bfs (startNode, kuronum):
    fila = []
    fila.append(startNode)
    fila.append(0)
    infected = [startNode]
    
    while (len(fila) > 0):
        server = fila.pop(0)
        distanceLayers = fila.pop(0)
        
        if distanceLayers == kuronum :
            return len(infected)
        
        for serverVizinho in server.vizinhos:
            if serverVizinho not in infected:
                fila.append(serverVizinho)
                fila.append(distanceLayers + 1)
                infected.append(serverVizinho)
    return -1
        
        

main()     