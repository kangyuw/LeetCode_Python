graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

queue = []

def bfs(root, visited):
    queue = [root]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

visited = set() # visited
for node in graph:
    if node not in visited:
        visited.add(node)
        bfs(node, visited)