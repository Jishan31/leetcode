class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, cols, diag1, diag2):
            if row == n: 
                return 1
            return sum(dfs(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
                       for col in range(n)
                       if col not in cols and row - col not in diag1 and row + col not in diag2)
                       
        return dfs(0, set(), set(), set())
        