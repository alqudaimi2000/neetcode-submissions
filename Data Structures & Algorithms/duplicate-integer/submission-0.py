class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for num in nums[i+1:]:
        #         if nums[i]==num:
        #             return True
        # return False
        numsSet=set(nums)
        return len(numsSet)!=len(nums)

        