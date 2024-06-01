class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        presum = [0]
        xor_sum = 0
        for num in arr:
            xor_sum ^= num
            presum.append(xor_sum)

        result = 0
        n = len(arr)
        for i in range(n):
            for k in range(i+1, n+1):
                if presum[i] == presum[k]:
                    result += k - i - 1

        return result

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        presum = defaultdict(list)
        xor_sum = 0
        seen = {0 : (1, 0)}
        ans = 0
        for i, num in enumerate(arr):
            xor_sum ^= num
            if xor_sum not in seen:
                seen[xor_sum] = (1, i+1)
            else:
                count, prev_sum = seen[xor_sum]
                ans += count * (i+1) - count - prev_sum
                count += 1
                prev_sum += i + 1
                seen[xor_sum] = (count, prev_sum)
        
        return ans
        