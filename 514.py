# url: https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        char_pos = defaultdict(list)
        for i, c in enumerate(ring):
            char_pos[c].append(i)

        def bisect_left(arr, key):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] < key:
                    start = mid + 1
                else:
                    end = mid - 1
            return end

        @functools.lru_cache(None)
        def rotate(ri, ki):
            if ki == m:
                return 0
            curr_char = key[ki]
            curr_char_indices = char_pos[curr_char]
            k = len(curr_char_indices)
            left = bisect_left(curr_char_indices, ri) % k
            right = (left + 1) % k
            left = curr_char_indices[left]
            right = curr_char_indices[right]
            right_moves = right - ri if right >= ri else n - ri + right
            left_moves = ri - left if ri >= left else n - left + ri
            return min(right_moves + 1 + rotate(right, ki+1), left_moves + 1 + rotate(left, ki+1))

        return rotate(0, 0)
