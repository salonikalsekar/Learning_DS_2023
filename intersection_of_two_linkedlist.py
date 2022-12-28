# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen = set()

        while headA != None:
            if headA in seen:
                return headA
            else:
                seen.add(headA)
            headA = headA.next

        while headB != None:
            if headB in seen:
                return headB
            else:
                seen.add(headB)

            headB = headB.next

        return

