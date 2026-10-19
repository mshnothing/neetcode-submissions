class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=False
        
        if set(s) != set(t):
            return res

        for ch in s:
            count=s.count(ch)
            if t.count(ch) != count:
                return res
        
        res=True
        return res