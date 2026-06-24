class Solution(object):
    def oddEvenList(self, head):
      
        if not head:
            return head
        odd_head = head
        cur_odd = odd_head
        odd_tail = cur_odd
        even_head = head.next
        cur_even = even_head

        while cur_even and cur_even.next:
            cur_odd.next = cur_odd.next.next
            cur_odd = cur_odd.next

            cur_even.next = cur_even.next.next
            cur_even = cur_even.next
        
        cur_odd.next = even_head

        return odd_head