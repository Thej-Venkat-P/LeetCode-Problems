# url: https://leetcode.com/problems/car-fleet/


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort()
        fleets = []
        for curr_pos, curr_vel in ps:
            time = (target - curr_pos) / curr_vel
            while fleets and fleets[-1] <= time:
                fleets.pop()
            fleets.append(time)
        return len(fleets)