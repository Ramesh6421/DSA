# selling profit V
# problem: link(https://www.codingninjas.com/codestudio/problems/rahul-and-his-chocolates_3118974?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
# exactly similar to the problem stocks profit II , the change is consider the fee for every transaction.

'''
Given chocolate and its prices change each day. Rahul can buy one chocolate at a time,
and he must sell it before buying chocolate on another day.
To sell and buy the chocolate requires some transaction fee.
Given 'N' number of days and an array 'PRICES' of size 'N' price of the chocolate each day.
and variable 'FEE' fee for the transaction.
Find the maximum profit Rahul can achieve by trading on the chocolate.

Example:
Input: 'N' = 3, 'PRICES' = [1, 2, 3], 'FEE' = 1
Output: 1

We can generate the maximum profit of 1 cent by buying the chocolate on the first day for price = 1 and then selling it on the third day for price = 3.                                                                                                     
The profit will be: 3 - 1 - 1(transaction fee) = 1

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
        pick =( arr[i] - fee ) + stock(i+1,1,arr,n,dp)
        nonpick = 0+ stock(i+1,0,arr,n,dp)
        profit = max(pick,nonpick)
        
    dp[i][buy] = profit
    return profit

n=3
fee = 1
prices=[1,2,3]
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
                pick = (arr[i] - fee) + dp[i+1][1]
                nonpick = 0+ dp[i+1][0]
                profit = max(pick,nonpick)
                
            dp[i][j] = profit
    return dp[0][1]        
            
                
n=3
fee = 1
prices=[1,2,3]
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
                pick = (arr[i] - fee) + prev[1]
                nonpick = 0+ prev[0]
                profit = max(pick,nonpick)
                
            cur[j] = profit
        prev = cur    
    return prev[1]        
n=3
fee = 1
prices=[1,2,3]
prev=[0 for j in range(2)]
print(stock(prices,n,prev))




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
        
        pick = (arr[i] - fee) + aheadbuy
        nonpick = 0+ aheadnotbuy
        curnotbuy = max(pick,nonpick)

        aheadbuy,aheadnotbuy=curbuy,curnotbuy
        
    return aheadbuy       

n=3
fee = 1
prices=[1,2,3]
print(stock(prices,n))        

            
