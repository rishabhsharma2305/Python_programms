def subset_sum(arr,target):
    n= len(arr)
    dp=[[None *(target+1)] *(n+1)]
    for i in range(n+1):
        dp[i][0]= True
    for i in range(1,target+1):
        dp[0][i]=False
    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i-1][j]
    return dp[n][target]
def min_sub_diff(arr):
    n=len(arr)
    temp=[]
    largest= sum(arr)
    for i in range(largest+1):
        if subset_sum(arr,i):
            temp.append(i)
    ans= sys.maxsize
    for i in temp:
        if ans>(largest-2(i)):
            ans= largest-2(i)
    return ans

if __name__=='__main__':
    print(min_sub_diff([6,5,10,1]))