def subset_sum_dp(arr,target,n):
    dp=[[None for i in range(target+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]= True
    for i in range(1,target+1):
        dp[0][i]= False
    for i in range(1,n+1):
        for j in range(1,target+1):
            
            if arr[i-1]<=j:
                #suppose i=5. then mere paas 5 elements hai toh mai 4rth index check karunga
                dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]= dp[i-1][j]
    return dp[n][target]
def subset_sum_rec(arr,target,n):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return subset_sum_rec(arr,target,n-1)
    else:
        return subset_sum_rec(arr,target,n-1) or subset_sum_rec(arr,target-arr[n-1],n-1)

if __name__=='__main__':
    print ( subset_sum_rec( [10,20,30] , 50 , 3 ) )
    print ( subset_sum_dp( [10,20,30] , 50 , 3 ) )
