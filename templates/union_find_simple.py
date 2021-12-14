# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/319459/Python3-UnionFindDFSBFS-solution
def countComponenets(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    
    for x, y in edges:
        union(x, y)
    
    return len({find(i) for i in range(n)})


n = 5
edges = [[0,1],[1,2],[3,4]]
ans = countComponenets(n, edges)
print(ans)