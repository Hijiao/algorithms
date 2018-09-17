package L0206;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class ReverseLinkedList {

    ListNode newHead = null;


    public ListNode reverseList(ListNode head) {

        if (head == null) {
            return null;
        }

        ListNode next;
        ListNode pre = head;

        ListNode cur = pre.next;
        pre.next = null;


        while (cur != null) {
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }

        return pre;

    }


    public ListNode reverseListRecursively(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode tail = recursiveCore(head);
        tail.next = null;
        return this.newHead;
    }

    private ListNode recursiveCore(ListNode node) {
        if (node.next == null) {
            this.newHead = node;

        } else {
            recursiveCore(node.next);
            node.next.next = node;
        }
        return node;
    }
}
