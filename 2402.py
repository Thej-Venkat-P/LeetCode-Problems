# url: https://leetcode.com/problems/the-most-booked-hotel-room/

import heapq
from collections import deque


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        busy = []
        counts = [0] * n
        
        for start, end in meetings:
            
            while busy and busy[0][0] <= start:
                end_prev, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                curr_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (curr_end + end - start, room))

            counts[room] += 1

        return counts.index(max(counts))
