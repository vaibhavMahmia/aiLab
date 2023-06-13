def depth_first_search(graph, start_node, target_node, visited=None):
    if visited is None:
        visited = set()  # Set to track visited nodes

    if start_node == target_node:
        return True  # Target node found

    visited.add(start_node)  # Mark current node as visited

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, target_node, visited):
                return True  # Target node found

    return False  # Target node not found
