def combinationSum(candidates,target):
        ans=[]
        def combination_sum(candidates,n,i,target,subset):
            if i==n:
                if target==0:
                    ans.append(subset)
                return 

            if candidates[i]<=target:
            #can pick at most target/candidates[i]
                combination_sum(candidates,n,i,target-candidates[i],subset+[candidates[i]])

            #not pick
            combination_sum(candidates,n,i+1,target,subset)
        i=0
        n=len(candidates)
        combination_sum(candidates,n,i,target,subset=[])
        return ans
print(combinationSum([1,4,9],13))    
    
