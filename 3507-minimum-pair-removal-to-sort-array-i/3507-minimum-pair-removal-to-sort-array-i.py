class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while nums != sorted(nums):
            i = min(range(len(nums) - 1), key=lambda x: nums[x] + nums[x + 1])
            nums[i:i + 2] = [nums[i] + nums[i + 1]]
            ops += 1
        return ops
        