# dfsPractice.py
def dfs(v,graph,visited):
    if visited[v]:
        return
    visited[v] = True
    print(v,end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor,graph,visited)
numv = int(input())
nume = int(input())
graph = {i:set() for i in range(numv)}
for _ in range(nume):
    x,y = map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)

for g in graph.keys():
    print(g,graph[g])

visited = [False for _ in range(numv)]
startv = int(input("Start at: "))
# visited[startv] = True
dfs(startv,graph,visited)
