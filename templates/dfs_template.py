# DFS for Tree

# Inorder Traversal

def inorder_iterative(root):
    result = []
    stack = []
    while (stack or root):
        while (root):
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result

def inorder_recursive(root, result):
    if not root:
        return
    inorder_recursive(root.left, result)
    result.append(root.val)
    inorder_recursive(root.right, result)

# Preorder Traversal

def preorder_iterative(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

def preorder_recursive(root, result):
    if not root:
        return
    result.append(root.val)
    preorder_recursive(root.left, result)
    preorder_recursive(root.right, result)

# Postorder Traversal

def postorder_iterative(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.insert(0, node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

def postorder_recursive(root,result):
    if not root:
        return
    postorder_recursive(root.left, result)
    postorder_recursive(root.right, result)
    result.append(root.val, result)

# DFS for graph

def dfs_graph(node, visited):
    # Check Boundary
    for neighbor in node.neighbors:
        dfs_graph(neighbor, visited)
    visited.add(node)
    return