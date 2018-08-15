package leetcode.L0687;

/**
 * Created by Max on 2018/8/8.
 */
public class LongestUnivaluePath {

    private class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private int max = 0;

    private void core(TreeNode node, int parentVal, int count) {
        if (node == null) {
            return;
        }
        if (node.val == parentVal) {
            max = max > count + 1 ? max : count + 1;
            core(node.left, node.val, count + 1);
            core(node.right, node.val, count + 1);

        } else {
            core(node.left, node.val, 0);
            core(node.right, node.val, 0);

        }

    }

    public int longestUnivaluePath(TreeNode root) {
        if (root == null) {
            return 0;
        }
        core(root.left, root.val, 0);
        core(root.right, root.val, 0);
        return max;

    }
}
