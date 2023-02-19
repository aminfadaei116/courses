

def BFS(graph, nodes, s, e):
    queue = []
    for i in nodes:
        if s in nodes[i]:
            start = i
    queue.append([start, 1])
    while queue:
        u = queue.pop(0)
        if e in nodes[u[0]]:
            return u[1]
        for i in graph[u[0]]:
            queue.append([i, u[1] + 1])
    return -1

def main():
    n = int(input())
    nodes = {}
    graph = {}
    for i in range(n):
        a = list(map(int, input().split()))
        nodes[i] = set(a)
        edges = []
        for j in graph:
            if nodes[j] & nodes[i]:
                edges += [j]
                graph[j] += [i]
        graph[i] = edges

    a, b = list(map(int, input().split()))
    print(BFS(graph, nodes, a, b))

if __name__ == '__main__':
    main()