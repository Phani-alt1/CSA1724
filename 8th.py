def dfs(graph,start):
    visited=set()
    stack=[start]
    result=[]

    while stack:
        node=stack.pop()
        if node not in visited:
            result.append(node)
            visited.add(node)
            stack.extend(reversed(graph[node]))
    return result

graph ={
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
print("DFS: ",dfs(graph,'A'))
