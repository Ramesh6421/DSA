# atmost 2-transactions(B-S,B-S)
# problem: link(https://www.codingninjas.com/codestudio/problems/buy-and-sell-stock_1071012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are Harshad Mehta’s friend. He told you the price of a particular stock for the next ‘N’ days.
You can either buy or sell a stock. Also, you can only complete at most 2-transactions.
Find the maximum profit that you can earn from these transactions. You can take help from Mr. Mehta as well.

Note
1. Buying a stock and then selling it is called one transaction. 
2. You are not allowed to do multiple transactions at the same time. This means you have to sell the stock before buying it again. 

Input:                       output:         B S     B S
prices=[7,1,5,3,6,4]            7      i.e, (1-5) + (3-6) = 4+3 = 7

'''
# Approach-1
'''
2-transaction
i.e,
                B  S  B  S
   trans =2        1     0

'''
# Recursion + Memoization
'''
TC-> O(N*2*3)
SC-> O(N*2*3) + O(N)
'''
def stock(i,buy,cap,arr,n,dp):
    if cap==0:
        return 0
    if i==n:
        return 0
    if dp[i][buy][cap]!=-1:
        return dp[i][buy][cap]
    profit = 0
    if buy==1:
        pick = -arr[i] + stock(i+1,0,cap,arr,n,dp)
        nonpick = 0+ stock(i+1,1,cap,arr,n,dp)
        profit = max(pick,nonpick)
        
    else:
        pick = arr[i] + stock(i+1,1,cap-1,arr,n,dp)
        nonpick = 0+ stock(i+1,0,cap,arr,n,dp)
        profit = max(pick,nonpick)
        
    dp[i][buy][cap] = profit
    return profit

n=6
prices=[7,1,5,3,6,4]
dp=[[[-1 for j in range(3)]for j in range(2)] for i in range(n)]
print(stock(0,1,2,prices,n,dp))
        

# Tabulation
'''
TC-> O(N*2*3)
SC-> O(N*2*3)
'''
def stock(arr,n,dp):
    # already declared as zero, no need to declare base cases
    '''for i in range(n+1):
        for j in range(2):
            dp[i][j][0]=0
    for j in range(2):
        for k in range(3):
            dp[n][j][k]=0 '''
    for i in range(n-1,-1,-1):
        for j in range(2):
            for k in range(1,3):
                if j==1:
                    pick = -arr[i]+dp[i+1][0][k]
                    nonpick = dp[i+1][1][k]
                    profit = max(pick,nonpick)
                    dp[i][j][k]=profit
                else:
                    pick = arr[i]+dp[i+1][1][k-1]
                    nonpick = dp[i+1][0][k]
                    profit = max(pick,nonpick)
                    dp[i][j][k]=profit
    return dp[0][1][2]            
n=6
prices=[7,1,5,3,6,4]
dp=[[[0 for j in range(3)]for j in range(2)] for i in range(n+1)]
print(stock(prices,n,dp))
        


# Space optimization
'''
TC-> O(N*2*3)
SC-> O(2*3)
'''
def stock(arr,n,after):
    # already declared as zero, no need to declare base cases
    '''for i in range(n+1):
        for j in range(2):
            dp[i][j][0]=0
    for j in range(2):
        for k in range(3):
            dp[n][j][k]=0 '''
    for i in range(n-1,-1,-1):
        cur=[[0 for j in range(3)]for j in range(2)]
        for j in range(2):
            for k in range(1,3):
                if j==1:
                    pick = -arr[i]+after[0][k]
                    nonpick = after[1][k]
                    profit = max(pick,nonpick)
                    cur[j][k]=profit
                else:
                    pick = arr[i]+after[1][k-1]
                    nonpick = after[0][k]
                    profit = max(pick,nonpick)
                    cur[j][k]=profit
        after=cur            
    return after[1][2]            
n=6
prices=[7,1,5,3,6,4]
after=[[0 for j in range(3)]for j in range(2)]
print(stock(prices,n,after))
        


# Approach-2
'''
2-transactions
i.e,  B  S  B  S
      0  1  2  3

      even for Buy
      odd for sell
'''

# Recursion + Memoization
'''
TC-> O(N*4)
SC-> O(N*4) + O(N)
'''
def stock(i,trans,arr,n,dp):
    if i==n or trans==4:
        return 0
    if dp[i][trans]!=-1:
        return dp[i][trans]
    if trans%2==0:
        pick = -arr[i] + stock(i+1,trans+1,arr,n,dp)
        nonpick = 0 + stock(i+1,trans,arr,n,dp)
        profit= max(pick,nonpick)
    else:
        pick = arr[i] + stock(i+1,trans+1,arr,n,dp)
        nonpick = 0 + stock(i+1,trans,arr,n,dp)
        profit= max(pick,nonpick)
    dp[i][trans]=profit    
    return profit

n=6
prices=[7,1,5,3,6,4]
dp=[[-1 for j in range(4)]for i in range(n)]
print(stock(0,0,prices,n,dp))
     

# Tabulation
'''
TC-> O(N*4)
SC-> O(N*4) 
'''

def stock(arr,n,dp):
    for i in range(n-1,-1,-1):
        for j in range(3,-1,-1):
            if j%2==0:
                pick = -arr[i] + dp[i+1][j+1]
                nonpick = 0 + dp[i+1][j]
                profit= max(pick,nonpick)
            else:
                pick = arr[i] + dp[i+1][j+1]
                nonpick = 0 + dp[i+1][j]
                profit= max(pick,nonpick)
            dp[i][j]=profit
    #print(dp)        
    return dp[0][0]

n=6
prices=[7,1,5,3,6,4]
dp=[[0 for j in range(4+1)]for i in range(n+1)]
print(stock(prices,n,dp))


# Space optimization
'''
TC-> O(N*4)
SC-> O(4)
'''

def stock(arr,n,after):
    for i in range(n-1,-1,-1):
        cur=[0 for j in range(4+1)]
        for j in range(3,-1,-1):
            if j%2==0:
                pick = -arr[i] + after[j+1]
                nonpick = 0 + after[j]
                profit= max(pick,nonpick)
            else:
                pick = arr[i] + after[j+1]
                nonpick = 0 + after[j]
                profit= max(pick,nonpick)
            cur[j]=profit
        after=cur
    return after[0]

n=6
prices=[7,1,5,3,6,4]
after=[0 for j in range(4+1)]
print(stock(prices,n,after))
     

                
