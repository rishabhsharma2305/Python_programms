def count_subset(arr,target,n):
    dp=[[None for i in range(target+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]= 1
    for i in range(1,target+1):
        dp[0][i]= 0
    for i in range(1,n+1):
        for j in range(1,target+1):
            
            if arr[i-1]<=j:
                #suppose i=5. then mere paas 5 elements hai toh mai 4rth index check karunga
                dp[i][j]= dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]= dp[i-1][j]
    return dp[n][target]
if __name__=='__main__':
    print ( count_subset( [10,20,30,25,25] , 50 , 5 ) )