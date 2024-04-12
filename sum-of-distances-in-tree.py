from typing import List

def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        distances = [0] * n
        visited = [False] * n
        queue = [(start, 0)]
        visited[start] = True

        while queue:
            u, dist = queue.pop(0)
            distances[u] = dist

            for neighbor in graph[u]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        
        return distances

    totalDistances = [0] * n

    for u in range(n):
        distances = bfs(u)
        totalDistances[u] = sum(distances)

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