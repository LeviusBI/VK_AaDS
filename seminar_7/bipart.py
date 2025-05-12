def is_bipartite(graph):
    visited = {}
    parent = {}

    def dfs(u, p, depth):
        visited[u] = True
        parent[u] = p
        for v in graph.get(u, []):
            if v == p:
                continue
            if v not in visited:
                if dfs(v, u, depth + 1):
                    return True
            else:
                cycle_length = depth - (parent[v] is not None and parent[v] != u)
                cycle_length = depth - parent.get(v, -1)
                if cycle_length % 2 == 1:
                    return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None, 0):
                return False
    return True
