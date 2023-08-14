'''
K-th permutation
if n=3, the possible permutations are
[123,132,213,231,312,321]

if k==4, k-th permutation = 231
if k==6, k-th permutation = 321


'''

def getPermutation(n,k):
    numbers=[]
    fact=1
    for i in range(1,n):
        fact=fact*i
        numbers.append(i)
    numbers.append(n)
    ans=''
    k=k-1
    while True:
        val=k//fact
        ans=ans+str(numbers[val])
        numbers.pop(val)
        if len(numbers)==0:
            break
        k=k%fact
        fact=fact//len(numbers)
    return ans    

n,k=[int(x) for x in input().split()]
print(getPermutation(n,k))

