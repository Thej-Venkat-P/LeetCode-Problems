# url : https://leetcode.com/problems/hand-of-straights/


from heapq import heapify, heappop, heappush
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        keys = list(count.keys())
        heapify(keys)

        while keys:
            first = heappop(keys)
            if first not in count or count[first] == 0:
                continue
            occ = count[first]
            for i in range(groupSize):
                if (first + i) not in count or count[first + i] < occ:
                    return False
                count[first + i] -= occ
        
        return True
            
