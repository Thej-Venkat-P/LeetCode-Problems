# url: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        differences = [0]*101

        for pos in seats:
            differences[pos] += 1
        
        for pos in students:
            differences[pos] -= 1

        moves = 0
        unmatched = 0
        for diff in differences:
            unmatched += diff
            moves += abs(unmatched)
            
        return moves