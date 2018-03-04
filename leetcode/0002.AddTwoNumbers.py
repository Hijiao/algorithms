# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        r = ListNode(0)
        curr = r.next
        carry = 0
        while p is not None and q is not None or carry != 0:
            sum = p.val if p else 0 + q.val if q else 0 +carry
            curr = ListNode(sum % 10)
            curr = curr.next
            carry = sum / 10
            p = p.next
            q = q.next
        while p is not None or carry != 0:
            sum = p.val if p else 0 + carry
            curr = ListNode(sum % 10)
            curr = curr.next
            carry = sum / 10
            p = p.next
        while q is not None or carry != 0:
            sum =q.val if q else 0 + carry
            curr = ListNode(sum % 10)
            curr = curr.next
            carry = sum / 10
            q = q.next
        return r.next


p = None
q = ListNode(1)

s = p.val if p else 0 + q.val if q else 0
print s
{}.has_key()