# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        
        dummy_head = ListNode(-1, head)
        pre_of_middle, slow, fast = dummy_head, head, head

        while fast and fast.next:

            pre_of_middle = slow
            slow = slow.next
            fast = fast.next.next

        junction = slow.next
        pre_of_middle.next = junction

        del slow

        return dummy_head.next
        