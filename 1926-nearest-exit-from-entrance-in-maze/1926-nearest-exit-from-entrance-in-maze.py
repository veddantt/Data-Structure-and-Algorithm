class Solution(object):
    def nearestExit(self, maze, entrance):
        
        directions= [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m= len(maze)
        n = len(maze[0])
        visited = [0]*(m*n)
        #bfs
        from collections import deque
        q = deque()
        q.append((tuple(entrance), 0))
        visited[entrance[0]*n + entrance[1]]=1
        while q:
            l, level = q.popleft()
            for direc in directions:
                x = l[0]+direc[0]
                y = l[1]+direc[1]
                if 0<=x<m and 0<= y<n:
                     if maze[x][y]=='.' and not visited[x*n+y]:
                        visited[x*n+y] = 1
                        q.append(((x, y), level+1))
                        if x==0 or x==m-1 or y==n-1 or y ==0:
                            return level+1
        return -1