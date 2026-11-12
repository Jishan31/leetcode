

class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        return [
            f"{num}/{den}"
            for den in range(2, n + 1)
            for num in range(1, den)
            if math.gcd(num, den) == 1
        ]