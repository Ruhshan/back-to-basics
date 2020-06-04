
ordering = []

def dfs(vertex, visited, graph):
    global ordering

    if visited[vertex] == "PARTIAL":
        return False
    
    if graph.get(vertex)!=None:
        visited[vertex] = "PARTIAL"
        for v in graph[vertex]:
            if visited[v] == "NOTVISITED":
                if dfs(v, visited, graph)== False:
                    return False
            if visited[v] == "PARTIAL":
                return False
                
        visited[vertex] ="VISITED"
        ordering.append(vertex)
    else:
        visited[vertex] = "VISITED"
        ordering.append(vertex)
    return True


if __name__ == "__main__":
    graph = {}
    visited = {}
    for v in "abcdef":
        visited[v]="NOTVISITED"

    for e,v in [("a","d"),("f","b"),("b","d"),("f", "a"),("d","c"),("e","a")]:
        if graph.get(e)!=None:
            graph[e].append(v)
        else:
            graph[e]=[v]
    for k in visited.keys():
        if visited[k]=="NOTVISITED":
            res = dfs(k,visited, graph)
    
    print(ordering[::-1])
    print(res)     
    
    