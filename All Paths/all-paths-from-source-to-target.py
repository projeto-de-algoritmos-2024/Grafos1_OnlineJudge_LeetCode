def bfs(graph):
    n = len(graph)
    queue = [(0, [0])]
    paths = []

    while queue:
        (u, path) = queue.pop(0)
        if u == n - 1:
            paths.append(path)
        for neighbour in graph[u]:
            if neighbour not in path:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append((neighbour, new_path))

    return paths

def main ():
    # N = quantidade de arestas
    N = int(input())
    graph = {}

    for _ in range(N):
        X, Y = map(int, input().split())

        if X in graph:
            graph[X].append(Y)
        else:
            graph[X] = [Y]

        if Y not in graph:
            graph[Y] = []

    print(graph)
    print(bfs(graph))

if __name__ == "__main__":
    main()