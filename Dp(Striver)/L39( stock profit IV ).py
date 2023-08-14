# problem: link(https://www.codingninjas.com/codestudio/problems/highway-billboards_3125969?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given a list of stock prices, ‘prices’. Where ‘prices[i]’ represents the price on ‘i’th day.
Your task is to calculate the maximum profit you can earn by trading stocks
if you can only hold one stock at a time. After you sell your stock on the ‘i’th day,
you can only buy another stock on ‘i + 2’ th day or later.

For Example:
You are given prices = {4, 9, 0, 4, 10},
To get maximum profits you will have to buy on day 0 and sell on day 1 to make a profit of 5,
and then you have to buy on day 3  and sell on day 4 to make the total profit of 11.
Hence the maximum profit is 11.

'''
# Recursion + Memoization
'''
TC-> O(N*2)
SC-> O(N*2) + O(N)
'''
def stock(ind,arr,n,cap,dp):
    if ind>=n:
        return 0
    if dp[ind][cap]!=-1:
        return dp[ind][cap]
    if cap==1:
        pick = -arr[ind] + stock(ind+1,arr,n,0,dp)
        nonpick = 0 + stock(ind+1,arr,n,1,dp)
        profit = max(pick,nonpick)
    else:
        pick = arr[ind] + stock(ind+2,arr,n,1,dp)
        nonpick = 0 + stock(ind+1,arr,n,0,dp)
        profit = max(pick,nonpick)
    dp[ind][cap]=profit    
    return profit

n=5
prices = [4,9,0,4,10]
dp=[[-1 for j in range(2)] for i in range(n)]
print(stock(0,prices,n,1,dp))
    
    
    
# Tabulation
'''
TC-> O(N*2)
SC-> O(N*2) 
'''    
def stock(n,arr,dp):
    for ind in range(n-1,-1,-1):
        for cap in range(2):
            if cap==1:
                pick = -arr[ind] + dp[ind+1][0]
                nonpick = 0 + dp[ind+1][1]
                profit = max(pick,nonpick)
            else:
                pick = arr[ind] + dp[ind+2][1]
                nonpick = 0 + dp[ind+1][0]
                profit = max(pick,nonpick)
            dp[ind][cap]=profit
    return dp[0][1]

            
n=5
prices = [4,9,0,4,10]
dp=[[0 for j in range(2)] for i in range(n+2)]
print(stock(n,prices,dp))


# Space Optimization
'''
TC-> O(N*2)
SC->  O(6)
'''
def stock(n,arr):
    front2 = [0 for j in range(2)]
    front1 = [0 for j in range(2)]
    for ind in range(n-1,-1,-1):
        cur = [0 for j in range(2)]
        for cap in range(2):
            if cap==1:
                pick = -arr[ind] + front1[0]
                nonpick = 0 + front1[1]
                profit = max(pick,nonpick)
            else:
                pick = arr[ind] + front2[1]
                nonpick = 0 + front1[0]
                profit = max(pick,nonpick)
            cur[cap]=profit
        front2 = front1
        front1 = cur
    return cur[1]

            
n=5
prices = [4,9,0,4,10]
print(stock(n,prices))
        
    

# Space Optimization
'''
TC-> O(N*2)
SC->  O(6)
'''
def stock(n,arr,dp):
    for ind in range(n-1,-1,-1):
        #Buy
        pick = -arr[ind] + dp[ind+1][0]
        nonpick = 0 + dp[ind+1][1]
        dp[ind][1] = max(pick,nonpick)
        #Sell
        pick = arr[ind] + dp[ind+2][1]
        nonpick = 0 + dp[ind+1][0]
        dp[ind][0] = max(pick,nonpick)
            
    return dp[0][1]

            
n=5
prices = [4,9,0,4,10]
dp=[[0 for j in range(2)] for i in range(n+2)]
print(stock(n,prices,dp))
