def routeExists(graph, startNode, endNode):
    queue = []
    queue.append(startNode)
    visited = {}
    visited[startNode] = True 

    while len(queue) != 0:
        for v in graph[startNode]:
            if v == endNode:
                return True
            else:
                if visited.get(v) != True:
                    queue.append(v)
        startNode = queue.pop(0)

        if graph.get(startNode)==None:
            return False
        visited[startNode] = True
    return False



if __name__ == "__main__":
    graph = {
        1:[2],
        2:[4],
        4:[5,6],
        5:[7],
        6:[13],
        17:[28]

    }

    print(routeExists(graph,1,17))

