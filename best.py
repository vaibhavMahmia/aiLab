from queue import PriorityQueue

def best_first_search(graph, start_node, target_node, heuristic):
    visited = set()  # Set to track visited nodes
    queue = PriorityQueue()  # Priority queue to store nodes for traversal
    queue.put((0, start_node))  # Add the start node to the queue with priority 0

    while not queue.empty():
        _, current_node = queue.get()  # Get the next node from the priority queue

        if current_node == target_node:
            return True  # Target node found

        if current_node not in visited:
            visited.add(current_node)  # Mark current node as visited

            # Add neighboring nodes to the priority queue with their respective heuristic values
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    priority = heuristic[neighbor]
                    queue.put((priority, neighbor))

    return False  # Target node not found
