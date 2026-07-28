class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        res = []

        for i in range(len(nums)):
            op = 0
            for j in range(len(nums)):
                if nums[j] == nums[i] or nums[i] == 0:
                    continue
                op = nums[j]
            res.append(op)
        return res
        ''' 
        # [1,2,3,4]
        res = []

        for i in range(len(nums)):
            op = 1
            arr = nums.copy()
            print(arr.pop(i))
            
            for j in range(len(arr)):
                op *= arr[j]
            res.append(op)
        return res

