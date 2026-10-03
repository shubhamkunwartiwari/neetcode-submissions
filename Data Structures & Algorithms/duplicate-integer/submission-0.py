class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a= nums.copy()
        dub=0
        for i in nums:
            a.remove(i)
            if i in a:
               dub+=1
               break 
        if dub>=1:
            return True
        else: 
            return False
