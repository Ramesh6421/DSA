# problem: link(https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1)
'''
Given a set of N jobs where each jobi has a deadline and profit associated with it.
Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
We earn the profit associated with job if and only if the job is completed by its deadline.
Find the number of jobs done and the maximum profit.

Example:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
'''
# Complexity
'''
TC-> O(NlogN)+O(N*N)
SC-> O(M)
'''
def solve(Jobs,N):
    Jobs.sort(key=lambda x:x[2],reverse=True)
    maxi=Jobs[0][1]
    for i in range(1,N):
        maxi=max(maxi,Jobs[i][1])
    res=[-1]*(maxi+1)
    jobcount=0
    jobprofit=0
    for i in range(N):
        for j in range(Jobs[i][1],0,-1):
            if res[j]==-1:
                res[j]=i
                jobcount+=1
                jobprofit+=Jobs[i][2]
                break
    return [jobcount,jobprofit]     

N = 4
Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
print(solve(Jobs,N))
