     
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

# 打印树
def print_bst(root): 

    def recursion(res,root):
        if not root:  res.append(None)
        res.append(root.val)
        if root.left:
            recursion(res,root.left)
        if root.right:
            recursion(res,root.right)

    res = []
    recursion( res,root)
    return res
 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#定义节点
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getBSTree(self, nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        root.left = self.getBSTree(left)
        root.right = self.getBSTree(right)

        return root

if __name__ == "__main__":
    solution = Solution()
    nums = [-10,-3,0,5,9] 
    root = solution.getBSTree(nums)
    res = print_bst(root)
    print(res)