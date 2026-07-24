class Solution:

    def uniqueXorTriplets(self, nums: list[int]) -> int:
        one = set(nums)
        two = {x ^ y for x in one for y in nums}
        three = {x ^ y for x in two for y in nums}
        return len(three)