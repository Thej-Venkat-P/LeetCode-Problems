class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def find_score(word):
            sc = 0
            for char in word:
                sc += score[ord(char) - ord('a')]
            return sc

        word_score = [find_score(word) for word in words]
        words_len = len(words)
        letter_count = Counter(letters)

        def check(word, letters_left):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letters_left[char]:
                    return False
            return True
        
        def remove(word, letters_left):
            for char in word:
                letters_left[char] -= 1
        
        def add(word, letters_left):
            for char in word:
                letters_left[char] += 1
        
        ans = [0]
        def backtrack(i, letter_count, curr_score):
            if i == words_len:
                if curr_score > ans[0]:
                    ans[0] = curr_score
                return
            word = words[i]
            if check(word, letter_count):
                remove(word, letter_count)
                backtrack(i+1, letter_count, curr_score + word_score[i])
                add(word, letter_count)
            backtrack(i+1, letter_count, curr_score)
            return score
        
        backtrack(0, letter_count, 0)
        return ans[0]    