class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        all_strings = []

        
        def backtrack(curr_string, i, chosen_strings):
            if i == n:
                if curr_string == "":
                    all_strings.append(" ".join(chosen_strings))
                return
            curr_string += s[i]
            if curr_string in wordDict:
                chosen_strings.append(curr_string)
                backtrack("", i+1, chosen_strings)
                chosen_strings.pop()
            backtrack(curr_string, i+1, chosen_strings)
        
        backtrack("", 0, [])
        return all_strings

