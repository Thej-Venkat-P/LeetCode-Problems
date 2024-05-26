class Solution:
    def checkRecord(self, n: int) -> int:
        eligible = [[1, 1, 0], [1, 0, 0]]
        m = (10**9 + 7)
        for i in range(2, n+1):
            next_iter = [[0]*3 for _ in range(2)]
            #P
            next_iter[0][0] = (sum(eligible[0])) % m
            next_iter[1][0] = (sum(eligible[1])) % m
            #A
            next_iter[1][0] = (next_iter[1][0] + next_iter[0][0]) % m
            #L
            next_iter[0][1] = (eligible[0][0]) % m
            next_iter[1][1] = (eligible[1][0]) % m
            next_iter[0][2] = (eligible[0][1]) % m
            next_iter[1][2] = (eligible[1][1]) % m

            eligible = next_iter
        
        s = sum([sum(elem) for elem in eligible])
        return s % m