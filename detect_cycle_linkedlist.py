# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:

            slow = fast = head

            while fast:
                if fast.next:
                    fast = fast.next.next
                else:
                    return False
                if slow == fast:
                    return True
                slow = slow.next

        return False
