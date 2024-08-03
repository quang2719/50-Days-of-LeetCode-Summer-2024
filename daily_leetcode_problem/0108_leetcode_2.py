# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        root = res
        note = 0
        while l1 or l2 or note:
            num1,num2  =0,0
            if l1:
                num1 = l1.val
                l1 = l1.next

            if l2:
                num2 = l2.val
                l2 = l2.next
            num3 = num1+num2+note
            note = 0
            if num3 >=10:
                res.val = num3%10
                note = 1
            else:
                res.val = num3
            if l1 or l2 or note:
                res.next = ListNode(None)
                res = res.next
        return root

# 1234 - 4321
# 12 - 21
# 4342 - 2434