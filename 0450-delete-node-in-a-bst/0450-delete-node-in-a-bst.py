class Solution(object):
    def deleteNode(self, root, key):
        def next_successor(root):
            root=root.right
            while root is not None and root.left is not None:
                root=root.left
            return root
        
        def del_node(root,k):
            if not root:
                return None
            
            if root.val>k:
                root.left=del_node(root.left,k)
            elif root.val<k:
                root.right=del_node(root.right,k)
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                
                succ=next_successor(root)
                root.val=succ.val
                root.right=del_node(root.right,succ.val)
            return root
            

        root=del_node(root,key)
        return root

        