# Prerequisites Tasks
# problem link(https://practice.geeksforgeeks.org/problems/prerequisite-tasks/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=prerequisite-tasks)
'''
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites,
for example to do task 0 you have to first complete task 1,
which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.

Input: 
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes
Explanation:
To do task 1 you should have completed
task 0, and to do task 2 you should 
have finished task 1, and to do task 3 you 
should have finished task 2. So it is possible.
Example 2:

Input:
N = 2, P = 2
prerequisites = {{1,0},{0,1}}
Output:
No
Explanation:
To do task 1 you should have completed
task 0, and to do task 0 you should
have finished task 1. So it is impossible.

'''
# NOTE
'''
The problem is similar to topological sort.(DFS/BFS)
if we found a cycle in given prerequisites, then we can't finish all tasks. otherwise we can.
'''
# L23 solution
def topo_Bfs_Detect_Cycle_I(V,adj):
    indegree=[0]*V
    for i in range(V):
        for j in adj[i]:
            indegree[j]+=1
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
        
    count=0
    while q:
        node=q.pop(0)
        count+=1
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
    if count==V:
        return 1
    return 0

N = 4
P = 3
prerequisites = [[1,0],[2,1],[3,2]]

adj={}
for i in range(N):
    adj[i]=[]
for u,v in prerequisites:
    adj[u].append(v)
print(topo_Bfs_Detect_Cycle_I(N,adj))
    

# Course Schedule
# problem link(https://practice.geeksforgeeks.org/problems/course-schedule/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=course-schedule)
'''
There are a total of n tasks you have to pick, labeled from 0 to n-1.
Some tasks may have prerequisites tasks, for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m.
Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all tasks, return an empty array.
Returning any correct order will give the output as 1, whereas any invalid order will give the output 0.

Input:
n = 2, m = 1
prerequisites = {{1, 0}}
Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible order is [0, 1].

Input:
n = 4, m = 4
prerequisites = {{1, 0},
                 {2, 0},
                 {3, 1},
                 {3, 2}}
Output:
1
Explanation:
There are a total of 4 tasks to pick.
To pick task 3 you should have finished
both tasks 1 and 2. Both tasks 1 and 2
should be pick after you finished task 0.
So one correct task order is [0, 1, 2, 3].
Another correct ordering is [0, 2, 1, 3].
Returning any of these order will result in
a Output of 1.

'''

# NOTE
'''
the problem is similar to Topological sort. In topological, u should be before v.
the given statement is v should be before u.( that is the only change ).
if no cycle exists, then return toposort ordering.
else, return empty array.

'''

def topo_Bfs_Detect_Cycle_II(V,adj):
    indegree=[0]*V
    for i in range(V):
        for j in adj[i]:
            indegree[j]+=1
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
        
    topo=[]
    while q:
        node=q.pop(0)
        topo.append(node)
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
    if len(topo)==V:
        return topo
    return []

n = 4
m = 4
prerequisites = [[1, 0],
                 [2, 0],
                 [3, 1],
                 [3, 2]]

adj={}
for i in range(n):
    adj[i]=[]
for u,v in prerequisites:
    adj[v].append(u)
print(topo_Bfs_Detect_Cycle_II(n,adj))
