def lcs_rec(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1+lcs_rec(x,y,n-1,m-1)
    return max(lcs_rec(x,y,n,m-1),lcs_rec(x,y,n-1,m))
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
    # return dp[n][m]
    return dp       # in case for printing
def print_lcs(x,y,n,m):
    dp= lcs_dp(x,y,n,m)
    i,j=n,m
    ans=""
    while i>0 and j>0:
        # if element are equal add it in string
        if x[i-1]==y[j-1]:
            ans+= x[i-1]
            i-=1
            j-=1
        else:
            # if element in left cell > upper cell then move left
            if dp[i][j-1]>dp[i-1][j]:
                j-=1
            # if element in left cell < upper cell then move up
            else:
                i-=1
    # because we are starting from the end
    return ans[::-1]

if __name__=='__main__':
    x='abcdefgh'
    y='axcyezgh'
    n,m= len(x),len(y)
    # print(lcs_rec(x,y,n,m))
    # print(lcs_dp(x,y,n,m))
    print(print_lcs(x,y,n,m))
    