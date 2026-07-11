class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        for x in t:
            if x in l:
                i = l.index(x)
                l.pop(i)
            else:
                return False
        if len(l) != 0:
            return False
        return True