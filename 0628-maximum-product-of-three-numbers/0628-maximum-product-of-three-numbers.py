

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max3 = heapq.nlargest(3, nums)
        min2 = heapq.nsmallest(2, nums)
        return max(max3[0] * max3[1] * max3[2], min2[0] * min2[1] * max3[0])