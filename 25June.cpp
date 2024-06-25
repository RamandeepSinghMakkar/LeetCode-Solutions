# Time Complexity: O(n)
# Space Complexity: O(logn)

#LeetCode Question Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/?envType=daily-question&envId=2024-06-25

# 1038. Binary Search Tree to Greater Sum Tree (Medium)

#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
#As a reminder, a binary search tree is a tree that satisfies these constraints:
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

class Solution {
 public:
  TreeNode* bstToGst(TreeNode* root) {
    int prefix = 0;

    function<void(TreeNode*)> reversedInorder = [&](TreeNode* root) {
      if (root == nullptr)
        return;

      reversedInorder(root->right);

      root->val += prefix;
      prefix = root->val;

      reversedInorder(root->left);
    };

    reversedInorder(root);
    return root;
  }
};
