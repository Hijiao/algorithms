package L0872;

import base.TreeNode;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class LeafSimilarTrees {

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        }
        if (root1 == null) {
            return false;
        }
        if (root2 == null) {
            return false;
        }
        Stack<TreeNode> stack = new Stack<>();
        Queue<TreeNode> queue = new LinkedList<>();
        stack.push(root1);

        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node.left != null) {
                stack.push(node.left);
            }
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.right == null && node.left == null) {
                queue.offer(node);
            }
        }
        stack.push(root2);

        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node.left != null) {
                stack.push(node.left);
            }
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.right == null && node.left == null) {
                TreeNode wanted = queue.poll();
                if (wanted == null || wanted.val != node.val) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(new LeafSimilarTrees().leafSimilar(null, new TreeNode(1)));
    }

}
