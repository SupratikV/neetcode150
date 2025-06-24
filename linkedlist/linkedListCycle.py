# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node=head
        s=set()      
        while node:
            # print("next is:",node.next.val)
            if node.val in s:
                return True
            s.add(node.val)
            node=node.next
        return False
        





        