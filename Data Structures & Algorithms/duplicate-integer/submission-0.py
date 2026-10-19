class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False

        res = len(set(nums)) != len(nums)
        return res
    
    