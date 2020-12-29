# 链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# 例如，给出
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 限制：
# 0 <= 节点个数 <= 5000



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1. 分治递归法
# - 思想：
# - 找到各个子树的根节点 root
# - 构建该根节点的左子树
# - 构建该根节点的右子树
# - 时间复杂度：O(n)
# - 空间复杂度：O(n)

class Solution(object):
    @classmethod
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder: return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0]) 
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid_idx = inorder.index(preorder[0])  
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid_idx+1], inorder[:mid_idx])   
        # 构建右子树
        root.right = self.buildTree(preorder[mid_idx+1:], inorder[mid_idx+1:])
        return root

# 2. 迭代法


class Solution(object):
    @classmethod
    def buildTree(self, preorder, inorder) -> TreeNode:


def main():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    final = Solution.buildTree(preorder, inorder)
    print(final)


if __name__ == "__main__":
    main()