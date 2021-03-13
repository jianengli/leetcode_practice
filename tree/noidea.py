记录不会的题目

练习：二叉查找树中第 K 小的元素 II
给定一个二叉搜索树，我们希望找到其中第 k 小的元素。

在这道题目中，除了原始的二叉搜索树 root 以外，你还会得到一个和其结构完全一致的二叉树 nodenum_root，树上节点的值代表以该节点为根的子树的节点数量。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/high-frequency-algorithm-exercise/5hhxs5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def kthSmallestII(self, root: TreeNode, nodenum_root: TreeNode, k: int) -> int:
        def demo(root, nodenum_root, k):
            if nodenum_root.val < k:
                return
            if nodenum_root.right:
                if nodenum_root.val - nodenum_root.right.val == k:
                    return root.val
                elif nodenum_root.val - nodenum_root.right.val < k:
                    return demo(root.right, nodenum_root.right, k-nodenum_root.val+nodenum_root.right.val)
                else:
                    return demo(root.left, nodenum_root.left, k)
            else:
                if nodenum_root.val == k:
                    return root.val
                elif nodenum_root.val > k:
                    return demo(root.left, nodenum_root.left, k)
        return demo(root, nodenum_root, k)
 