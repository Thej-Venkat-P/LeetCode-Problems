# url: https://leetcode.com/problems/find-common-characters/


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = Counter(words[0])
        for word in words[1:]:
            word_count = Counter(word)
            for char in chars:
                if char in word_count:
                    chars[char] = min(chars[char], word_count[char])
                else:
                    chars[char] = 0
        
        ans = []
        for char in chars:
            for _ in range(chars[char]):
                ans.append(char)
        return ans