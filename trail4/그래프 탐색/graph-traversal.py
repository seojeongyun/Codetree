n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)


def dfs(start_node, graph,visited):
    for nxt in graph[start_node]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt,graph,visited)
    return sum(visited) - 1 if sum(visited) >=1 else 0
visited = [0]*(n+1)
print(dfs(1,graph,visited))