class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1,2,3,4,4,6,7,8,9,10
        res = 1
        
        n = set(nums)
        nums = list(n)
        nums.sort()
        d =[]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i]+1 in nums:
                d.append(nums[i])
                d.append(nums[i]+1)
            else:
                d = []
            
            if res < len(set(d)):
                res = len(set(d))
        return res