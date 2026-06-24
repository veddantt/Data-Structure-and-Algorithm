class Solution(object):
    def pairSum(self, head):
        ans = 0
        newList = None
        current = head
        currHalf = head

        while currHalf and currHalf.next:
            currHalf = currHalf.next.next
            temp = current.next
            current.next = newList
            newList = current
            current = temp

        while current:
            ans = max(ans, current.val + newList.val)
            current = current.next
            newList = newList.next
        
        return ans