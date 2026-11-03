class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
    
        return sorted(list(s))==sorted(list(t))
        # sSorted=list(s)
        # tSorted=list(t)
        # sSorted.sort()
        # tSorted.sort()
        # return sSorted==tSorted