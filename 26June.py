# Time Complexity: O(n)
# Space Complexity: O(n)

# LeetCode Question Link: https://leetcode.com/problems/balance-a-binary-search-tree/description/

# 1382. Balance a Binary Search Tree (Medium)

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

class Solution:
  def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    nums = []

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return
      inorder(root.left)
      nums.append(root.val)
      inorder(root.right)

    inorder(root)

    # Same as 108. Convert Sorted Array to Binary Search Tree
    def build(l: int, r: int) -> Optional[TreeNode]:
      if l > r:
        return None
      m = (l + r) // 2
      return TreeNode(nums[m],
                      build(l, m - 1),
                      build(m + 1, r))

    return build(0, len(nums) - 1)
