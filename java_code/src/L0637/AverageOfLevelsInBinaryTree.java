package L0637;


import java.util.*;
import base.TreeNode;

public class AverageOfLevelsInBinaryTree {


    public List<Double> averageOfLevels(TreeNode root) {
        if (root == null) {
            return Collections.emptyList();
        }
        Queue<TreeNode> queue = new LinkedList<>();
        List<Double> list = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int count = queue.size();
            int total = 0;
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                total += node.val;
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
                list.add((double)total / count);

        }

        return list;

    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);

        root.right = new TreeNode(20);
        root.right.right = new TreeNode(7);
        root.right.left= new TreeNode(15);

        System.out.println(new AverageOfLevelsInBinaryTree().averageOfLevels(root));

    }

}
