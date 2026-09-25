# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while True: 
            min_index = -1
            min_value = 0
            i = 0
            while i < len(lists):
                if lists[i] is not None: 
                    if min_index == -1:
                        min_index = i
                        min_value = lists[i].val
                    else:
                        if lists[i].val<min_value:
                            min_index = i
                            min_value = lists[i].val
                i += 1

            if min_index == -1:
                break
            smallest_node = lists[min_index]

            lists[min_index] = smallest_node.next
            smallest_node.next = None
            tail.next = smallest_node
            tail = tail.next
        return dummy.next
                        
        