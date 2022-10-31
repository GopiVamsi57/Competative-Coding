from typing import *

def DFS(visited,dict,source):
    s = [source]
    visited[source]=1
    cluster=[]
    while(s):
        source = s.pop(-1)
        cluster.append(source)
        for i in dict[source]:
            if(visited[i]==0):
                visited[i]=1
                s.append(i)
    return cluster,visited
    
def depthFirstSearch(V: int, E: int, edges: List[Dict[int, int]]):
    # write your code here
    
    dict={}
    for i in range(V):
        dict[i]=[]
    for a,b in edges:
        dict[a].append(b)
        dict[b].append(a)
    for i in dict:
        dict[i] = sorted(dict[i])
    visited = [0]*V
    count = 0
    clusters=[]
    for i in range(V):
        if visited[i]==0:
            count+=1
            source=i
            cluster,visited = DFS(visited,dict,source)
            clusters.append(sorted(cluster))
  
    return clusters
    pass
