import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        total_ones = s.count('1')
        blocks = []
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0': j += 1
                blocks.append((i, j - 1, j - i))
                i = j
            else: i += 1
                
        m = len(blocks)
        if m < 2: return [total_ones] * len(queries)
            
        L, R, z = [b[0] for b in blocks], [b[1] for b in blocks], [b[2] for b in blocks]
        
        K = m - 1
        LOG = K.bit_length()
        st = [[0] * LOG for _ in range(K)]
        for i in range(K): st[i][0] = z[i] + z[i + 1]
        for j in range(1, LOG):
            for i in range(K - (1 << j) + 1):
                st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
                
        def rmq(l, r):
            if l > r: return 0
            j = (r - l + 1).bit_length() - 1
            return max(st[l][j], st[r - (1 << j) + 1][j])
            
        ans = []
        for ql, qr in queries:
            i = bisect.bisect_left(R, ql)
            j = bisect.bisect_right(L, qr) - 1
            
            if i >= j or i >= m or j < 0:
                ans.append(total_ones)
                continue
                
            zi, zj = R[i] - max(L[i], ql) + 1, min(R[j], qr) - L[j] + 1
            if j - i == 1:
                ans.append(total_ones + zi + zj)
                continue
                
            best = max(zi + z[i + 1], z[j - 1] + zj, rmq(i + 1, j - 2))
            ans.append(total_ones + best)
            
        return ans