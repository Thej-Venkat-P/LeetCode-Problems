# url: https://leetcode.com/problems/find-all-people-with-meetings-in-a-given-time-range/


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = {0, firstPerson} 
        
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
            stack = set()
            graph = defaultdict(list)
            for x, y, _ in grp: 
                graph[x].append(y)
                graph[y].append(x)
                if x in dic: stack.add(x)
                if y in dic: stack.add(y)

            stack = list(stack)
            while stack: 
                x = stack.pop()
                for y in graph[x]: 
                    if y not in dic: 
                        dic.add(y)
                        stack.append(y)
        return dic


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = set([0,firstPerson])
        meetings.sort(key = lambda x: x[2])

        def all_people(meets):
            union_find = {}
            def parent(n):
                for i in union_find:
                    if n in union_find[i]:
                        return i
                else:
                    union_find[n] = set([n])
                    return n
            for a,b in meets:
                a = parent(a)
                b = parent(b)
                if a == b:
                    continue
                if a in ans:
                    union_find[a].update(union_find[b])
                    del union_find[b]
                else:
                    union_find[b].update(union_find[a])
                    del union_find[a]
            for i in union_find:
                if i in ans:
                    ans.update(union_find[i])

        prev_time = -1
        conc_meet = []
        for a,b,t in meetings:
            if t != prev_time:
                all_people(conc_meet)
                conc_meet = [(a,b)]
                prev_time = t
            else:
                conc_meet.append((a,b))
        all_people(conc_meet)

        return list(ans)