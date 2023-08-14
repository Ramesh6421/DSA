# problem: link(https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1)
'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 

Example 2:
Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.

'''
# Complexity
'''
TC-> O(NlogN)+(N)
SC-> O(1)
'''
def solve(W,Items,N):
    def aByb(item):
        return item[0]/item[1]
    Items.sort(key=aByb,reverse=True)   # sorting based on (value/weight) in reverse order
    ans=0
    i=0
    while W>0 and i<N:
        if Items[i][1]<=W:
            ans+=Items[i][0]
            W-=Items[i][1]
        else:
            k=(Items[i][0]/Items[i][1])*W   # taking some part 
            ans+=k
            break
        i+=1
    return ans

N = 3
W = 50
Items=[(60,10),(100,20),(120,30)]  # [(value,weight)]
print(solve(W,Items,N))
