def is_safe(region, color, assignment, neighbors):
    for neighbor in neighbors.get(region, []):
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment

    region = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:
                return result
            assignment.pop(region)
    return None

regions = ['A', 'B', 'C']
neighbors = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
colors = ['Red', 'Green']

solution = backtrack({}, regions, colors, neighbors)

if solution:
    for region in regions:
        print(region + ":", solution[region])
else:
    print("No solution found")
