from collections import deque

def breadth_first_search(graph, start_node, target_node):
    visited = set()  # Set to track visited nodes
    queue = deque()  # Queue to store nodes for traversal
    queue.append(start_node)  # Add the start node to the queue

    while queue:
        current_node = queue.popleft()  # Get the next node from the front of the queue

        if current_node == target_node:
            return True  # Target node found

        if current_node not in visited:
            visited.add(current_node)  # Mark current node as visited

            # Add neighboring nodes to the queue
            queue.extend(graph[current_node])

    return False  # Target node not found

