from collections import Counter
from math import factorial
from string import ascii_lowercase


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        m = len(s) // 2
        freq = Counter(s[:m])

        perm = factorial(m)
        for v in freq.values():
            perm //= factorial(v)

        if k > perm:
            return ""

        half = ""
        for i in range(m):
            for c in ascii_lowercase:
                if not freq[c]:
                    continue
                cnt = perm * freq[c] // (m - i)
                if k <= cnt:
                    freq[c] -= 1
                    half += c
                    perm = cnt
                    break
                k -= cnt

        mid = s[m] if len(s) % 2 else ""
        return half + mid + half[::-1]