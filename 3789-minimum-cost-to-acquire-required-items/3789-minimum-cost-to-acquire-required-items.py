class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 <= costBoth:
            return cost1 * need1 + cost2 * need2
        
        cnt_3 = min(need1, need2)
        total_cost = cnt_3 * costBoth
        need1 -= cnt_3
        need2 -= cnt_3
        
        if need1 > 0:
            total_cost += need1 * min(cost1, costBoth)
        elif need2 > 0:
            total_cost += need2 * min(cost2, costBoth)
            
        return total_cost