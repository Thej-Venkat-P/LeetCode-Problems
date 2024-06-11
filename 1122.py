# url: https://leetcode.com/problems/relative-sort-array


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2d = {val: i for i, val in enumerate(arr2)}
        occ = defaultdict(int)
        rest = []
        for num in arr1:
            if num in arr2:
                occ[arr2d[num]] += 1
            else:
                rest.append(num)
        rest.sort()
        ans = []
        for i in range(len(arr2)):
            for j in range(occ[i]):
                ans.append(arr2[i])
        ans += rest
        return ans


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 = {val: i for i, val in enumerate(arr2)}
        for num in arr1:
            if num not in arr2:
                arr2[num] = 1000 + num
        arr1.sort(key=lambda x: arr2[x])
        return arr1