# url: https://leetcode.com/problems/task-scheduler/


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(collections.Counter(tasks).values())
        counts.sort(reverse = True)
        idle_groups = counts[0] - 1
        idle = (idle_groups) * n

        for c in counts[1:]:
            idle -= min(idle_groups, c)
        
        idle = idle if idle > 0 else 0

        return len(tasks) + idle