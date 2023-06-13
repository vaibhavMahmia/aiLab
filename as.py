import heapq


def a_star(graph, start_node, goal_node):
    open_set = [(0, start_node)]  # Priority queue to store nodes for traversal
    came_from = {}  # Map to store the previous node in the optimal path
    g_scores = {node: float('inf') for node in graph}  # Map to store the cost from the start node to each node
    g_scores[start_node] = 0  # Cost from start node to itself is 0

    while open_set:
        _, current_node = heapq.heappop(open_set)  # Get the node with the smallest f-score

        if current_node == goal_node:
            # Reconstruct the path from goal to start
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start_node)
            path.reverse()
            return path

        for neighbor, weight in graph[current_node].items():
            g_score = g_scores[current_node] + weight  # Calculate the cost to reach the neighbor
            if g_score < g_scores[neighbor]:
                # Update the path to the neighbor as a better path has been found
                came_from[neighbor] = current_node
                g_scores[neighbor] = g_score
                f_score = g_score + heuristic(neighbor, goal_node)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path found

