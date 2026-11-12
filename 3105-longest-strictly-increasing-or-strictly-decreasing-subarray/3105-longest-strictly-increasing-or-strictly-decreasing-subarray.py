class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = max_len = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc, dec = inc + 1, 1
            elif nums[i + 1] < nums[i]:
                inc, dec = 1, dec + 1
            else:
                inc = dec = 1
            max_len = max(max_len, inc, dec)
        return max_len