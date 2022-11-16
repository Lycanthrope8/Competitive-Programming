# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line

## These are slow processes

def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []


##This are fast processes

  class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
      res, stack = [], [(root, False)]
      while stack:
        node, visited = stack.pop()  # the last element
        if node:
          if visited:
            res.append(node.val)
          else:  # preorder: root -> left -> right
            stack.append((node.right, False))
            stack.append((node.left, False))
            stack.append((node, True))
      return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
      res, stack = [], [(root, False)]
      while stack:
        node, visited = stack.pop()  # the last element
        if node:
          if visited:
            res.append(node.val)
          else:  # inorder: left -> root -> right
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
      return res


