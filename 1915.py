class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  # 2^10 to store XOR values
        result = 0
        prefix_xor = 0
        count[prefix_xor] = 1
        
        for char in word:
            char_index = ord(char) - ord('a')
            prefix_xor ^= 1 << char_index
            result += count[prefix_xor]
            for i in range(10):
                result += count[prefix_xor ^ (1 << i)]
            count[prefix_xor] += 1
        
        return result


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        result = 0
        curr_state = 0
        count[0] = 1

        for char in word:
            char_idx = ord(char) - ord('a')
            curr_state ^= 1 << char_idx
            count[curr_state] += 1

        for curr_state, val in count.items():
            result += val * (val - 1) // 2
            for i in range(10):
                new_state = curr_state ^ (1 << i)
                if new_state < curr_state:
                    new_val = count.get(new_state, 0)
                    result += val * new_val
        
        return result