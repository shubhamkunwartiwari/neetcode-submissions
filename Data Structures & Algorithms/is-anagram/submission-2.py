class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_1=[]
        seen_2=[]
        for i in s:
            seen_1.append(i)
        for i in t:
            seen_2.append(i)
        seen_1=sorted(seen_1)
        seen_2=sorted(seen_2)
        if seen_1==seen_2:
            return True 
        return False