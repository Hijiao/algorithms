# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, p = None, None
        # if l1 is not None and l2 is not None:
        #     if (l1.val > l2.val):
        #         head = l2
        #         l2 = l2.next
        #     else:
        #         head = l1
        #         l1 = l1.next
        # elif l1 is not None:
        #     return l1
        #
        # elif l2 is not None:
        #     return l2
        # else:
        #     return None
        # p = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        # if (l1 is not None):
        #     p.next = l1
        # else:
        #     p.next = l2
        p.next = l1 or l2
        return head.next


if __name__ == "__main__":
    l1 = [f]
    Solution().mergeTwoLists(None, None)
