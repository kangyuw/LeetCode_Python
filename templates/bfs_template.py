# BFS for Tree: Level-order traversal

from collections import deque

def level_order_traversal(root, result):
    if not root:
        return
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# BFS for Graph

def bfs_graph(root):
    if not root:
        return
    queue = deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        # do something with node
        # add all neighbors of node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return