def find_connected_component(graph):
    visited = set()
    components = []

    def dfs(v):
        visited.add(v)
        component.append(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node)
            components.append(component)

    return components

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
    4: [5],
    5: [4],
    6: []
}

print(find_connected_component(graph))
