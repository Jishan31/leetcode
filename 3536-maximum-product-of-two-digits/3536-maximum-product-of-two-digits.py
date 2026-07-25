class Solution:
 def maxProduct(self, n: int) -> int:
    return eval("*".join(sorted(str(n))[-2:]))