class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return False
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i] + nums[j] == target:
                    return [j,i]