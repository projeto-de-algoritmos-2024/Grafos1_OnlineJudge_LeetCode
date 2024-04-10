def bfs(graph, start, end, obstacle):
    queue = [(start, [start])]
    paths = []

    while queue:
        (node, path) = queue.pop(0)
        if node == end and obstacle not in path:
            paths.append(path)
            break
        for neighbour in graph[node]:
            if neighbour not in path:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append((neighbour, new_path))

    return paths

def main ():
    N, A, B, C = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        X, Y = map(int, input().split())
        
        graph[X].append(Y)
        graph[Y].append(X)
    
    pathsAforB = bfs(graph, A, B, C)
    pathsAforC = bfs(graph, A, C, B)

    probability = len(pathsAforB) / (len(pathsAforB) + len(pathsAforC))
    print(f"{probability:.6f}")

if __name__ == "__main__":
    main()