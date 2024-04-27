# url: https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        degree = [0]*n
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            degree[a] += 1
            degree[b] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])

        remaining = n

        while remaining > 2:
            no_of_leaves = len(leaves)
            remaining -= no_of_leaves
            for _ in range(no_of_leaves):
                leaf = leaves.popleft()
                neighbour = graph[leaf].pop()
                degree[leaf] = 0
                del graph[leaf]
                graph[neighbour].remove(leaf)
                degree[neighbour] -= 1
                if degree[neighbour] == 1:
                    leaves.append(neighbour)
        
        return list(graph.keys())
