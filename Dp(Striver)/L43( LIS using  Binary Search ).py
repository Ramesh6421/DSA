# length of LIS using binary search
# the final sequence is not the LIS but the length of LIS is correct.

import bisect
def LIS(arr,n):
    temp=[]
    temp.append(arr[0])
    for i in range(1,n):
        if arr[i]>temp[-1]:
            temp.append(arr[i])
        else:
            pos = bisect.bisect_left(temp,arr[i])
            temp[pos]=arr[i]
    return len(temp)

n=6
arr=[5,4,11,1,16,8]
#n = 8
#arr = [10,9,2,5,3,7,101,18]
print(LIS(arr,n))     
            
