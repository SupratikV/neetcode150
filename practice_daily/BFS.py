from collections import deque

#here graph is a dict where keys are nodes and values are the neighbouring nodes.
def dfs(graph,start):
    q=deque([start])
    visited=set()
    visited.add(start)

    while q:
        ele=q.popleft()
        for i in graph[ele]:
            if i not in visited:
                visited.add(i)
                q.append(i)
        

            

