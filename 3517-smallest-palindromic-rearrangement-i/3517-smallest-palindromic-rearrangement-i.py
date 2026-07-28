class Solution:
 def smallestPalindrome(self, s: str) -> str:
    k = len(s) // 2
    half = sorted(s[:k])
    return "".join(half) + s[k : len(s) - k] + "".join(reversed(half))