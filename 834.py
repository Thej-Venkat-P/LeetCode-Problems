# url: https://leetcode.com/problems/sum-of-distances-in-tree/


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = [1]*n
        res = [0]*n

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def reroot(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + n - count[child]
                    reroot(child, node)
                
        dfs(0, -1)
        reroot(0, -1)
        return res