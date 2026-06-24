class Solution(object):
    def leafSimilar(self, root1, root2):
        leaves1, leaves2 = [], []
        
        self.getLeaves(root1, leaves1)
        self.getLeaves(root2, leaves2)

        return leaves1 == leaves2

    def getLeaves(self, root, leaves):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaves.append(root.val)

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
