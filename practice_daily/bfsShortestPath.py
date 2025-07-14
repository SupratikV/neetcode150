#graph is a dictionary with key as node and values as neighbours
from collections import deque
def bfs(graph,start,end):
    visited=set([start])
    q=deque([(start,0)])# node,distance format
    while q:
        ele,dist=q.popleft()
        if ele==end:
            return dist
        for i in graph[ele]:
            q.append((i,dist+1))
            visited.add(i)
    return -1
