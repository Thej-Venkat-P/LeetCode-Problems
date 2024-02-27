# url: https://leetcode.com/problems/encode-and-decode-strings/
# Question Number: 271


class Codec:
    def encode(self, strs: [str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> [str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1 + length
            ans.append(s[j + 1:i])