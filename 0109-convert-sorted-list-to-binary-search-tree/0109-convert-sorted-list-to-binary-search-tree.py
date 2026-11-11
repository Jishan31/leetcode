class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        vals = []
        while head: 
            vals, head = vals + [head.val], head.next
        
        def build(l, r):
            if l > r: return None
            mid = (l + r) // 2
            return TreeNode(vals[mid], build(l, mid - 1), build(mid + 1, r))
            
        return build(0, len(vals) - 1)