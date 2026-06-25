class Solution(object):
    def pathSum(self, root, targetSum):
        prefix={0:1}

        def travel(root,k,total):
            count=0
            if root is None:
                return 0
    

            total+=root.val
            x=total-k


            if x in prefix:
               count= prefix[x] 

            if total in prefix:
                prefix[total]+=1
            else:
                prefix[total]=1

            count+=travel(root.left,k,total)+travel(root.right,k,total)

            prefix[total]-=1

            return count  
        c=travel(root,targetSum,0)   
        return c             