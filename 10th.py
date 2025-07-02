graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 1},
    'E': {'G': 2},
    'F': {'G': 5},
    'G': {}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 4, 'E': 3, 'F': 6,
    'G': 0
}

def a_star(start, goal):
    open_list = [start]
    came_from = {}
    g = {node: float('inf') for node in graph}
    g[start] = 0

    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristic[x])
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)

        for neighbor in graph[current]:
            new_g = g[current] + graph[current][neighbor]
            if new_g < g[neighbor]:
                g[neighbor] = new_g
                came_from[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

path = a_star('A', 'G')
print("Path:", " → ".join(path))
