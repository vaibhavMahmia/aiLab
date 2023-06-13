import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start_node] = 0  # Set the distance of the start node to 0
    queue = [(0, start_node)]  # Priority queue to store nodes for traversal

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get the node with the smallest distance

        # Skip if already visited
        if current_distance > distances[current_node]:
            continue

        # Traverse neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
