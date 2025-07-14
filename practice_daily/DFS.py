def dfs(node):
    if node in visited:
        visited.add(node)
    for i in graph[node]:
        if i not in visited:
            dfs(i)