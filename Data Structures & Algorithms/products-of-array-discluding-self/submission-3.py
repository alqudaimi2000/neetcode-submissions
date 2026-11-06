class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j=len(nums)-1
        pre,post,res=[1 for _ in range(len(nums))],[1 for _ in range(len(nums))],[1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if(i==0):
                pre[i]=nums[i]
                post[j]=nums[j]
                j-=1
            else:
                pre[i]=pre[i-1]*nums[i]
                post[j]=post[j+1]*nums[j]
                j-=1
        for i in range(len(nums)):
            if i == 0:
                res[i]=post[i+1]
            elif i==len(nums)-1:
                res[i]=pre[i-1]
            else:
                res[i]=post[i+1]*pre[i-1]
        return res



