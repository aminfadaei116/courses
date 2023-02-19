def DFS(graph, s, visited, path):
    global maxLen, maxPath
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = 1
            DFS(graph, i, visited, path + [i])
            visited[i] = 0
    if len(path) > maxLen:
        maxLen = len(path)
        maxPath = path

n = int(input())
edges = [[] for i in range(n)]
findEdge = {}
for i in range(n):
    tmp = input()
    if 's' + tmp[-1] in findEdge:
        edges[i] += findEdge['s' + tmp[-1]]
    if 'e' + tmp[0] in findEdge:
        for j in findEdge['e' + tmp[0]]:
            edges[j] += [i]
    if 's' + tmp[0] in findEdge:
        findEdge['s' + tmp[0]] += [i]
    else:
        findEdge['s' + tmp[0]] = [i]
    if 'e' + tmp[-1] in findEdge:
        findEdge['e' + tmp[-1]] += [i]
    else:
        findEdge['e' + tmp[-1]] = [i]

maxLen = 0
maxPath = []
visited = [0 for i in range(n)]
for i in range(n):
    visited[i] = 1
    DFS(edges, i, visited, [i])
    visited[i] = 0

print(edges)
print(findEdge)
if maxLen == n:
    print('possible')
else:
    print('not possible')
