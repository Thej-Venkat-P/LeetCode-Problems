# url: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)

        while students :
            while sandwiches[0] in set(students) and students[0] != sandwiches[0] :
                students.append(students.popleft())
            if sandwiches[0] == students[0] :
                students.popleft()
                sandwiches.popleft()
            else :
                break
        
        return len(students)

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_cnt = Counter(students)
        for sw in sandwiches :
            if stu_cnt[sw] :
                stu_cnt[sw] -= 1
            else :
                sw = 0 if sw else 1
                return stu_cnt[sw]
        return 0