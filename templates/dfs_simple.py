graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs(root, visited):
    visited.add(root)
    for neighbor in graph[root]:
        if neighbor not in visited:
            dfs(neighbor, visited)

visited = set()
for node in graph:
    if node not in visited:
        dfs(node, visited)