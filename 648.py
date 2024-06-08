# url: https://leetcode.com/problems/replace-words/


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            curr_trie = trie
            for ch in word:
                if ch not in curr_trie:
                    curr_trie[ch] = {}
                curr_trie = curr_trie[ch]
            curr_trie["#"] = word
        
        def derivative(word):
            curr_trie = trie
            for ch in word:
                if ch not in curr_trie:
                    return word
                curr_trie = curr_trie[ch]
                if "#" in curr_trie:
                    return curr_trie["#"]
            return word

        words = sentence.split()
        sentence = []
        for word in words:
            sentence.append(derivative(word))
        return " ".join(sentence)