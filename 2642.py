# url: https://leetcode.com/problems/design-graph-with-shortest-path-calculator


import heapq
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = collections.defaultdict(dict)
        self.n = n
        for edge in edges :
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        f,t,c = edge
        self.graph[f][t] = c

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n
        pq = [(0, node1)]
        dist[node1] = 0

        while pq :
            curr_cost, min_node = heapq.heappop(pq)
            if curr_cost > dist[min_node] :
                continue
            if min_node == node2 :
                return curr_cost
            for node in self.graph[min_node] :
                new_dist = dist[min_node] + self.graph[min_node][node]
                if new_dist < dist[node] :
                    dist[node] = new_dist
                    heapq.heappush(pq, (new_dist, node))
        return -1