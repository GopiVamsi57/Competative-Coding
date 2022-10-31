def BFS_recursive(visited,dict,source,bfs,q):
    q.append(source)
    visited[source]=1
    while(q):
        source = q.pop(0)
        bfs.append(source)
        for i in dict[source]:
            if(visited[i]==0):
                visited[i]=1
                q.append(i)
    return bfs,visited,q
    
def BFS(vertex, edges):
    # Write your solution here
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph 
    dict = {}
    for i in range(vertex):
        dict[i]=[]
    u = edges[0]
    v = edges[1]
    for i in range(len(u)):
        dict[u[i]].append(v[i])
        dict[v[i]].append(u[i])
    for i in dict:
        dict[i] = sorted(dict[i])
    
        
    bfs=[]
    visited = [0]*vertex
    q = []
    for i in range(vertex):
        if(visited[i]==0):
            source =i
            bfs,visited,q = BFS_recursive(visited,dict,source,bfs,q)
    return bfs
