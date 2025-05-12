def bellman_ford(graph, source):
    distance = {vertex: float('inf') for vertex in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] + weight < distance[neighbor]:
                return -1

    return distance

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -1), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}

distances = bellman_ford(graph, 'A')
print(distances)  # {'A': 0, 'B': 4, 'C': 2, 'D': 5}
