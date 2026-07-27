class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        op = []
        for num in nums:
            fre[num] = 1+fre.get(num,0)
        sorted_fre = sorted(fre.items(),key=lambda x: x[1],  reverse= True)
        for i in range(0,k):
            op.append(sorted_fre[i][0])
        return op