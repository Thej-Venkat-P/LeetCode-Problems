# url: https://leetcode.com/problems/open-the-lock/

from heapq import heapify, heappop, heappush
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ud = {str(i): (str((i+1)%10), str((i-1)%10)) for i in range(10)}
        def children(lock):
            res = []
            for i in range(4):
                add_val, sub_val = ud[lock[i]]
                res.append(lock[:i]+add_val+lock[i+1:])
                res.append(lock[:i]+sub_val+lock[i+1:])
            return res

        def dist(lock):
            curr_dist = 0
            for i in range(4):
                curr_val = int(lock[i])
                t_val = int(target[i])
                curr_dist += min((curr_val - t_val)%10, (t_val - curr_val)%10)
            return curr_dist

        visited = set(deadends)
        q = []
        q.append((dist("0000"), 0, "0000"))
        while q:
            d, turns, lock = heappop(q)
            if lock in visited:
                continue
            if lock == target:
                return turns
            visited.add(lock)
            for child in children(lock):
                if child not in visited:
                    heappush(q, (dist(child)+turns+1, turns+1, child))
        return -1