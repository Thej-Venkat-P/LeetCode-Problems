# url: https://leetcode.com/problems/word-search-ii/


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        words = set(words)
        mapping = collections.defaultdict(set)
        for word in words:
            for j in range(len(word)):
                mapping[word[:j]].add(word)

        ans = set()

        min_len = min(tuple(map(len, words)))
        if m*n < min_len:
            return []
        
        board_counts = collections.Counter(sum(board, []))
        words_copy = words.copy()
        for word in words_copy:
            word_counts = Counter(word)
            for c in word_counts:
                if word_counts[c] > board_counts[c]:
                    words.remove(word)
                    break

        found = set()
        def backtrack(s, i, j):
            if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in found:
                s += board[i][j]
            else:
                return False
            if s in words:
                ans.add(s)
            if s not in mapping:
                return False
            found.add((i, j))
            result = (
                backtrack(s, i+1, j) or
                backtrack(s, i-1, j) or
                backtrack(s, i, j+1) or
                backtrack(s, i, j-1)
            )
            found.remove((i, j))
            return result

        for i in range(m):
            for j in range(n):
                backtrack("", i, j)
        
        return list(ans)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        ans = []
        
        ref = set()
        for i in range(m):
            for j in range(n-1):
                ref.add(board[i][j] + board[i][j+1])
        for j in range(n):
            for i in range(m-1):
                ref.add(board[i][j] + board[i+1][j])

        trie = {}
        for word in words:
            found = True
            for j in range(len(word)-1):
                w_s = word[j:j+2]
                if w_s not in ref and w_s[::-1] not in ref:
                    found = False
                    break
            if not found:
                continue
                
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["end"] = word

        def backtrack(i, j, trie):
            char = board[i][j]
            if char not in trie:
                return 

            curr_trie = trie[char]
            word = curr_trie.pop("end", None)
            if word:
                ans.append(word)

            board[i][j] = ""
            if i > 0 :
                backtrack(i-1, j, curr_trie)
            if j > 0 :
                backtrack(i, j-1, curr_trie)
            if i < m-1 :
                backtrack(i+1, j, curr_trie)
            if j < n-1 :
                backtrack(i, j+1, curr_trie)
            board[i][j] = char

            if not curr_trie:
                trie.pop(char)
            return 

        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie)
        
        return list(ans)