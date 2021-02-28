class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = []
        maxlen = 0
        for i in list(s):
            if i not in out:
                out.append(i)
                if len(out) > maxlen:
                    maxlen = len(out)
            else:
                if len(out) > maxlen:
                    maxlen = len(out)
                next = out.index(i) + 1
                out = out[next:]
                out.append(i)
        return maxlen
