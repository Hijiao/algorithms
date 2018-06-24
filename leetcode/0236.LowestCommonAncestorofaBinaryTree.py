# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.found_p = False
        self.found_q = False
        self.p_path = []
        self.q_path = []
    def find_paths(self,root, p, q):
        if self.found_p and self.found_q:
            return
        if not self.found_p :
            self.p_path.append(root)
            if id(root) == id(p):
                self.found_p = True
        if not self.found_q:
            self.q_path.append(root)
            if id(root) ==id(q):
                self.found_q = True
        if root.left:
            self.find_paths(root.left,p,q)
        if root.right:
            self.find_paths(root.right,p,q)
        if not self.found_p:
            self.p_path.pop()
        if not self.found_q:
            self.q_path.pop()

    def find_common_path(self):
        common_index = 0
        for index in range(min(len(self.p_path),len(self.q_path))):
            if self.p_path[index] == self.q_path[index]:
                common_index = index
            else:
                return self.q_path[common_index]
        return self.q_path[common_index]


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.find_paths(root,p,q)
        r =  self.find_common_path().val
        return r
    def lowestCommonAncestor2(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right
r = TreeNode(1)
l = TreeNode(2)
r.left=l
print Solution().lowestCommonAncestor2(r,r,l).val