package leetcode.L0559;

import java.util.List;

/**
 * Created by Max on 2018/8/8.
 */
public class MaximumDepthOfNaryTree {
    private class Node {
        public int val;
        public List<Node> children;

        public Node() {
        }

        public Node(int _val, List<Node> _children) {
            val = _val;
            children = _children;
        }
    }

    public int getDepth(Node node) {
        if (node == null) {
            return 0;
        }
        int max = 0;
        for (Node n : node.children) {
            int d = getDepth(n);
            max = max >= d ? max : d;
        }
        return max + 1;
    }

    public int maxDepth(Node root) {
        return getDepth(root);
    }
}
