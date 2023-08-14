# maximum sum in grid with starting points(0,0),(0,c-1) and dest is last row , if both are at same cell only one will take that cell.
# problem: link(https://www.codingninjas.com/codestudio/problems/ninja-and-his-friends_3125885?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
# notes (https://takeuforward.org/data-structure/3-d-dp-ninja-and-his-friends-dp-13/)
'''
Ninja has a 'GRID' of size 'R' X 'C'. Each cell of the grid contains some chocolates.
Ninja has two friends Alice and Bob, and he wants to collect as many chocolates as possible with the help of his friends.
Initially, Alice is in the top-left position i.e. (0, 0), and Bob is in the top-right place i.e. (0, ‘C’ - 1) in the grid.
Each of them can move from their current cell to the cells just below them.
When anyone passes from any cell, he will pick all chocolates in it, and then the number of chocolates in that cell will become zero.
If both stay in the same cell, only one of them will pick the chocolates in it.
If Alice or Bob is at (i, j) then they can move to (i + 1, j), (i + 1, j - 1) or (i + 1, j + 1). They will always stay inside the ‘GRID’.
Your task is to find the maximum number of chocolates Ninja can collect with the help of his friends by following the above rules.

Example:
Input: ‘R’ = 3, ‘C’ = 4
       ‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
Output: 21
Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and will collect 2 + 4 + 6 = 12 chocolates.
Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3) and will colllect 2 + 2 + 5 = 9 chocolates.
Hence the total number of chocolates collected will be 12 + 9 = 21. there is no other possible way to collect a greater number of chocolates than 21.

'''
# Recursion
'''
TC-> (3**R) * (3**R)
SC-> O(R)
'''

# Recursion + Memoization
'''
TC-> O(R*C*C)*9
SC-> O(R*C*C) +O(R)
'''
def maxx(grid,r,c,i,j1,j2,dp):
    if j1<0 or j1>=c or j2<0 or j2>=c:
        return -(10**9+7)
    if i==r-1:
        if j1==j2:
            return grid[i][j1]
        else:
            return grid[i][j1]+grid[i][j2]
    if dp[i][j1][j2]!=-(10**9+7):
        return dp[i][j1][j2]
    maxi=-(10**9+7)    
    for dj1 in range(-1,2):
        for dj2 in range(-1,2):
            val=0
            if j1==j2:
                val=grid[i][j1]
            else:
                val=grid[i][j1]+grid[i][j2]
            val+=maxx(grid,r,c,i+1,j1+dj1,j2+dj2,dp)
            maxi=max(maxi,val)
    dp[i][j1][j2]=maxi
    return maxi        

grid=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
r,c=3,4
dp=[[[-(10**9+7) for k in range(c)]for k in range(c)]for k in range(c)]
print(maxx(grid,r,c,0,0,c-1,dp))


# Tabulation
'''
TC-> O(R*C*C)*9
SC-> O(R*C*C) 
'''
def maxx(r,c,grid,dp):
    for j1 in range(c):
        for j2 in range(c):
            if j1==j2:
                dp[r-1][j1][j2]=grid[r-1][j1]
            else:    
                dp[r-1][j1][j2]=grid[r-1][j1]+grid[r-1][j2]
    for i in range(r-2,-1,-1):
        for j1 in range(c):
            for j2 in range(c):
                maxi=-(10**9+7)    
                for dj1 in range(-1,2):
                    for dj2 in range(-1,2):
                        val=0
                        if j1==j2:
                            val=grid[i][j1]
                        else:
                            val=grid[i][j1]+grid[i][j2]
                        if j1+dj1>=0 and j1+dj1<c and j2+dj2>=0 and j2+dj2<c:    
                            val+=dp[i+1][j1+dj1][j2+dj2]
                        else:
                            val+=-(10**9+7)
                        maxi=max(maxi,val)
                dp[i][j1][j2]=maxi
    return dp[0][0][c-1]                
              
grid=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
r,c=3,4
dp=[[[-(10**9+7) for k in range(c)]for k in range(c)]for k in range(c)]
print(maxx(r,c,grid,dp))


# Space Optimization
'''
TC-> O(R*C*C)*9
SC-> O(C*C) 
'''

def maxx(r,c,grid,front):
    for j1 in range(c):
        for j2 in range(c):
            if j1==j2:
                front[j1][j2]=grid[r-1][j1]
            else:    
                front[j1][j2]=grid[r-1][j1]+grid[r-1][j2]
    for i in range(r-2,-1,-1):
        cur=[[-(10**9+7) for k in range(c)]for k in range(c)]
        for j1 in range(c):
            for j2 in range(c):
                maxi=-(10**9+7)    
                for dj1 in range(-1,2):
                    for dj2 in range(-1,2):
                        val=0
                        if j1==j2:
                            val=grid[i][j1]
                        else:
                            val=grid[i][j1]+grid[i][j2]
                        if j1+dj1>=0 and j1+dj1<c and j2+dj2>=0 and j2+dj2<c:    
                            val+=front[j1+dj1][j2+dj2]
                        else:
                            val+=-(10**9+7)
                        maxi=max(maxi,val)
                cur[j1][j2]=maxi
        front=cur
    return front[0][c-1]                
              
grid=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
r,c=3,4
front=[[-(10**9+7) for k in range(c)]for k in range(c)]
print(maxx(r,c,grid,front))


                            
