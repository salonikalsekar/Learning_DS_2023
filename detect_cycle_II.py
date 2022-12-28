# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            slow =  head.next
            fast = head.next.next

            while fast != slow:
                if fast != None and fast.next != None:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    return

            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return fast