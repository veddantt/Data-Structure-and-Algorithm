
class Solution(object):
    def equalPairs(self, grid):
        ans = 0 
        for j in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[j])
            ans+= grid.count(column) # count how many rows equal to this column
            
        return ans 