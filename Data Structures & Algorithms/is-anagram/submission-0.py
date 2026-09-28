class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countsT = {}
        if(len(t) != len(s)):
            return False
        for n in range (len(s)):
            counts[s[n]]=counts.get(s[n], 0) + 1
        for n in range (len(t)):
            countsT[t[n]]=countsT.get(t[n], 0) + 1
        return counts == countsT
        




        