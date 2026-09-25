# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: 
            return None
        if k == 1:
            return head

        nodes = []
        cur = head

        while cur is not None: 
            nodes.append(cur)
            cur = cur.next

        n = len(nodes)

        i = 0
        while i + k <= n:
            left = i
            right = i + k - 1

            while left < right :
                temp = nodes[left]
                nodes[left] = nodes[right]
                nodes[right] = temp
                left += 1
                right -= 1
            i += k
        idx = 0

        while idx < n - 1:
            nodes[idx].next = nodes[idx + 1]
            idx += 1
        
        nodes[n-1].next = None

        return nodes[0]