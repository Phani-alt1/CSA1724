import itertools

graph = {
    'A': {'A': 0,  'B': 10, 'C': 15},
    'B': {'A': 10, 'B': 0,  'C': 20},
    'C': {'A': 15, 'B': 20, 'C': 0}
}

cities = ['A', 'B', 'C']
start = 'A'

other_cities = [city for city in cities if city != start]
all_paths = itertools.permutations(other_cities)

min_cost = float('inf')
best_path = []

for path in all_paths:
    full_path = [start] + list(path) + [start]
    cost = 0
    for i in range(len(full_path) - 1):
        cost += graph[full_path[i]][full_path[i+1]]
    
    if cost < min_cost:
        min_cost = cost
        best_path = full_path

print("Shortest path:", " -> ".join(best_path))
print("Cost:", min_cost)
