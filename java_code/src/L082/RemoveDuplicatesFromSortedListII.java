package L082;

public class RemoveDuplicatesFromSortedListII {
    private class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode lastDisNode = null;
        ListNode newHead = null;
        ListNode checkpoint = head;

        while (checkpoint != null) {
            boolean skipped = false;
            while (checkpoint.next != null && checkpoint.next.val == checkpoint.val) {
                checkpoint = checkpoint.next;
                skipped = true;
            }
            if (skipped) {
                if (checkpoint.next == null && lastDisNode != null) {
                    lastDisNode.next = null;
                    break;
                } else {
                    checkpoint = checkpoint.next;
                }
            } else {
                if (newHead == null) {
                    newHead = checkpoint;
                    lastDisNode = checkpoint;
                } else {
                    lastDisNode.next = checkpoint;
                    lastDisNode = lastDisNode.next;
                }
                checkpoint = checkpoint.next;
            }
        }
        return newHead;

    }

    public ListNode deleteDuplicatesR(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        ListNode cur = head;

        while (cur != null) {
            if (cur.next != null && cur.next.val == cur.val) {
                int v = cur.val;
                while (cur != null && cur.val == v) {
                    cur = cur.next;
                }
                pre.next = cur;
            } else {
                pre = cur;
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}