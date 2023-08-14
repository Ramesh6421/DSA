# priblem : link(https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Ninja is planing this ‘N’ days-long training schedule.
Each day, he can perform any one of these three activities.
(Running, Fighting Practice or Learning New Moves).
Each activity has some merit points on each day.
As Ninja has to improve all his skills,
he can’t do the same activity in two consecutive days.
Can you help Ninja find out the maximum merit points Ninja can earn?
You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity.
Your task is to calculate the maximum number of merit points that Ninja can earn.

for example,
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.

Input:                       output:
2
3                                 11
1 2 5  
3 1 1
3 3 3
3                                 210
10 40 70
20 50 80
30 60 90

'''

# Recursion + Memoization approach
'''
TC-> O(N*4)*3
SC-> O(N) + O(N*4)
'''

def merit(arr,day,last,dp):
    if day==0:
        maxi=-1
        for i in range(3):
            if i!=last:
                val=arr[day][i]
                maxi=max(maxi,val)
        return maxi
    if dp[day][last]!=0:
        return dp[day][last]
    maxi=0
    for i in range(3):
        if i!=last:
            points=arr[day][i]+ merit(arr,day-1,i,dp)
            maxi=max(maxi,points)
    dp[day][last]=maxi
    return maxi

n=3
arr=[[1,2,5],[3,1,1],[3,3,3]]
day=n-1
last=3
dp=[[0 for i in range(4)]for j in range(n)]
print(merit(arr,day,last,dp))
            
# Tabulation approach
'''
TC-> O(N*4)*3
SC-> O(N*4)
'''
def merit(arr,n,dp):
    dp[0][0]=max(arr[0][1],arr[0][2])
    dp[0][1]=max(arr[0][0],arr[0][2])
    dp[0][2]=max(arr[0][0],arr[0][1])
    dp[0][3]=max(arr[0][0],arr[0][1],arr[0][2])
    for day in range(1,n):
        for last in range(4):
            maxi=0
            for task in range(3):
                if task!=last:
                    points=arr[day][task] + dp[day-1][task]
                    maxi=max(maxi,points)
            dp[day][last]=maxi

    return dp[n-1][3]        
            
    
n=3
arr=[[1,2,5],[3,1,1],[3,3,3]]
dp=[[0 for i in range(4)]for j in range(n)]
print(merit(arr,n,dp))
            

# space optimization approach
'''
TC-> O(N*4)*3
SC-> O(4)
'''
def merit(arr,n,prev):
    prev[0]=max(arr[0][1],arr[0][2])
    prev[1]=max(arr[0][0],arr[0][2])
    prev[2]=max(arr[0][0],arr[0][1])
    prev[3]=max(arr[0][0],arr[0][1],arr[0][2])
    for day in range(1,n):
        temp=[0 for i in range(4)]
        for last in range(4):
            maxi=0
            for task in range(3):
                if task!=last:
                    points=arr[day][task] + prev[task]
                    maxi=max(maxi,points)
            temp[last]=maxi
        prev=temp
    return prev[3]        
            
    
n=3
arr=[[1,2,5],[3,1,1],[3,3,3]]
prev=[0 for i in range(4)]
print(merit(arr,n,prev))
            
    
