def lcs_dp(x,y,n,m):
    #creat matrix[n+1][m+1]. dp[i][j] represent the lcs when lenght of string are i,j
    dp=[[None for i in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for i in range(m+1):
        dp[0][i]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]: # zero indexing 
                dp[i][j]= 1+dp[i-1][j-1]  # if last char is same then 1+ lcs in strings with len i-1 and j-1
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1]) #check for max string with i and j-1 or i-1,j len
    return dp[n][m]
if __name__=='__main__':
    x='heap'
    y='pea'
    length_of_lcs= lcs_dp(x,y,4,3)
    a= len(x)-length_of_lcs # deletions required to make x in lcs
    b= len(y)-length_of_lcs # insertions required to make y in lcs
    print(a+b)