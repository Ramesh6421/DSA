# stocks profit
# problrm: link(https://www.codingninjas.com/codestudio/problems/stocks-are-profitable_893405?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an array/list 'prices' where the elements of the array represent the prices of the stock
as they were yesterday and indices of the array represent minutes.
Your task is to find and return the maximum profit you can make by buying and selling the stock.
You can buy and sell the stock only once.

Note:
You can’t sell without buying first.

For Example:
For the given array [ 2, 100, 150, 120],
The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.
So, the output will be 148.

'''
# Complexities
'''
TC-> O(N)
sc->O(1)
'''
def profits(prices,n):
    mini=prices[0]
    profit=0
    for i in range(1,n):
        cost=prices[i]-mini
        profit=max(cost,profit)
        mini=min(mini,prices[i])
    return profit

n=6
prices=[7,1,5,3,6,4]
print(profits(prices,n))
