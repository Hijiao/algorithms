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
        curr = r
        carry = 0
        while p is not None or q is not None or carry != 0:
            pval = p.val if p else 0
            qval = q.val if q else 0
            sum = pval + qval + carry
            curr.next = ListNode(sum % 10)
            curr = curr.next
            carry = sum / 10
            p = p.next if p else None
            q = q.next if q else None
        return r.next
