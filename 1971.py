# url: https://leetcode.com/problems/find-if-path-exists-in-graph/

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        p = self.find_parent(self.parent[x])
        self.parent[x] = p
        return p

    def join(self, a, b):
        pa = self.find_parent(a)
        pb = self.find_parent(b)
        if pa == pb: return
        if self.size[pa] > self.size[pb]:
            self.size[pa] += self.size[pb]
            self.parent[pb] = pa
        else:
            self.size[pb] += self.size[pa]
            self.parent[pa] = pb
        
    def is_connected(self, a, b):
        return self.find_parent(a) == self.find_parent(b)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        uf = UnionFind(n)
        fs = fd = False
        for a, b in edges:
            uf.join(a, b)
            if source in (a,b):
                fs = True
            if source in (a, b):
                fd = True
            if fs and fd and uf.is_connected(source, destination):
                return True
        return False

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if [source, destination] in (edges):
            return True
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, found):
            if destination in found:
                return True
            for val in graph[node]:
                if val not in found:
                    found.add(val)
                    if dfs(val, found):
                        return True
            return False
        
        return dfs(source, set([source]))