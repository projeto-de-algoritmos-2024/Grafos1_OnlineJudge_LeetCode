def bfs(graph, start, end):
    queue = [(start, [start])]
    paths = []

    while queue:
        (node, path) = queue.pop(0)
        if node == end:
            paths.append(path)
        for neighbour in graph[node]:
            if neighbour not in path:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append((neighbour, new_path))

    return paths

def main ():
    N, A, B, C = map(int, input().split())

    graph = [[] for _ in range(0, N + 1)]
    for _ in range(0, N-1):
        X, Y = map(int, input().split())
        
        graph[X].append(Y)
        graph[Y].append(X)
    
    pathsAforB = bfs(graph, A, B)
    pathsAforC = bfs(graph, A, C)

    probability = format((len(pathsAforB) / 1) / (len(pathsAforB) + len(pathsAforC)), ".6f")
    print(probability)
    
if __name__ == "__main__":
    main()