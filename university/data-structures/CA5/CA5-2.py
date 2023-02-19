def BFS(graph, start, end):
    queue = []
    queue.append([start, 0])
    while queue:
        u = queue.pop(0)
        if u[0] == end:
            return u[1]
        for i in graph[u[0]]:
            queue.append([i, u[1] + 1])

n, m = list(map(int, input().split()))
graph = {}
l = {}
for i in range(n):
    for j in range(m):
        graph[(i*m)+j] = []
a, b, c = 0, 0, 0
while 1:
    a, b, c = list(map(int, input().split()))
    if a == b == c == -1:
        break
    if (n-a+1) % 2:
        l[((n-a-1)*m)+m-b-1] = c
    else:
        l[((n-a-1)*m)+b] = c
for i in graph:
    graph[i] = []
    f = True
    for j in range(6, 0, -1):
        if i + j < n * m:
            if i + j in l:
                graph[i] += [l[i+j]]
            elif i + j == m*n-1 or f:
                 graph[i] += [i+j]
                 f = False
print(BFS(graph, 0, m*n - 1))
