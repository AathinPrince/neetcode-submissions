class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        map1 = {}
        for i in range(0,l):
            b = target -nums[i]
            if b in map1:
                return [map1[b],i]
            else:
                map1[nums[i]] = i