# selling profit II
# problem: link(https://www.codingninjas.com/codestudio/problems/selling-stock_630282?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You have been given stock values/prices for N number of days.
Every i-th day signifies the price of a stock on that day.
Your task is to find the maximum profit which you can make by buying and selling the stocks.

Note :
You may make as many transactions as you want but can not have more than one transaction at a time
i.e, if you have the stock, you need to sell it first, and then only you can buy it again.

'''

# Recursion + Memoization
'''
TC-> O(N*2)
SC-> O(N*2)+O(N+2)
'''
def stock(i,buy,arr,n,dp):
    if i==n:
        return 0
    if dp[i][buy]!=-1:
        return dp[i][buy]
    profit = 0
    if buy==1:
        pick = -arr[i] + stock(i+1,0,arr,n,dp)
        nonpick = 0+ stock(i+1,1,arr,n,dp)
        profit = max(pick,nonpick)
        
    else:
        pick = arr[i] + stock(i+1,1,arr,n,dp)
        nonpick = 0+ stock(i+1,0,arr,n,dp)
        profit = max(pick,nonpick)
        
    dp[i][buy] = profit
    return profit

n=6
prices=[7,1,5,3,6,4]
dp=[[-1 for j in range(2)] for i in range(n)]
print(stock(0,1,prices,n,dp))
        


# Tabulation
'''
TC-> O(N*2)
SC-> O(N*2)
'''
def stock(arr,n,dp):
    dp[n][0]=0
    dp[n][1]=0
    for i in range(n-1,-1,-1):
        for j in range(2):
            if j==1:
                pick = -arr[i] + dp[i+1][0]
                nonpick = 0+ dp[i+1][1]
                profit = max(pick,nonpick)
                
            else:
                pick = arr[i] + dp[i+1][1]
                nonpick = 0+ dp[i+1][0]
                profit = max(pick,nonpick)
                
            dp[i][j] = profit
    return dp[0][1]        
            
                
n=6
prices=[7,1,5,3,6,4]
dp=[[0 for j in range(2)] for i in range(n+1)]
print(stock(prices,n,dp))
        



# Space Optimization using two rows
'''
TC-> O(N*2)
SC-> O(2)
'''
def stock(arr,n,prev):
    prev[0]=0
    prev[1]=0
    for i in range(n-1,-1,-1):
        cur = [0 for j in range(2)]
        for j in range(2):
            if j==1:
                pick = -arr[i] + prev[0]
                nonpick = 0+ prev[1]
                profit = max(pick,nonpick)
                
            else:
                pick = arr[i] + prev[1]
                nonpick = 0+ prev[0]
                profit = max(pick,nonpick)
                
            cur[j] = profit
        prev = cur    
    return prev[1]        
n=6
prices=[7,1,5,3,6,4]
prev=[0 for j in range(2)]
print(stock(prices,n,dp))




# Space Optimization using four variables
'''
TC-> O(N*2)
SC-> O(2)
'''
def stock(arr,n):
    aheadbuy=0
    aheadnotbuy=0
    for i in range(n-1,-1,-1):
        pick = -arr[i] + aheadnotbuy
        nonpick = 0+ aheadbuy
        curbuy = max(pick,nonpick)
        
        pick = arr[i] + aheadbuy
        nonpick = 0+ aheadnotbuy
        curnotbuy = max(pick,nonpick)

        aheadbuy,aheadnotbuy=curbuy,curnotbuy
        
    return aheadbuy       
n=6
prices=[7,1,5,3,6,4]
print(stock(prices,n))        

            
