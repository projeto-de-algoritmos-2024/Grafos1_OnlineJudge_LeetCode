from typing import List

def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]
    distances = [1] * n
    totalDistances = [0] * n

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(start, father):
        for neighbor in graph[start]:
            if neighbor != father:
                dfs(neighbor, start)
                distances[start] += distances[neighbor]
                totalDistances[start] += totalDistances[neighbor] + distances[neighbor]

    def dfsTwo(start, father):
        for neighbor in graph[start]:
            if neighbor != father:
                totalDistances[neighbor] = totalDistances[start] - distances[neighbor] + (n - distances[neighbor])
                dfsTwo(neighbor, start)

    dfs(0, -1)
    dfsTwo(0, -1)
    
    return totalDistances


def main():
    n = int(input())
    edges = []

    for _ in range(n - 1):
        edge = input().strip()
        u, v = map(int, edge.split())
        edges.append([u,v])

    print(sumOfDistancesInTree(n,edges))

if __name__ == "__main__":
    main()