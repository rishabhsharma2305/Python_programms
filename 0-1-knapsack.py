#Recursion
def knapsack_rec(weight,value,capacity,n):
    # if there is no element or no capacity then profit would be 0
    if n==0 or capacity==0:
        return 0
    # start from n-1th element. if its wieght is less <= capacity then there are 2 choices. either it could be added or not base upon the max profit
    if weight[n-1]<=capacity:
                     # if the element is choosen, Capacity would reduce by choosen element wieght.if the element not choosen, no capacity would reduce. it simply check for rest of the array
        return max( ( value[n-1] + knapsack_rec(weight,value,capacity-weight[n-1],n-1)) , knapsack_rec(weight,value,capacity,n-1) )
    else:
        knapsack_rec(weight,value,capacity,n-1)

def knapsack_dp(weight,value,capacity,n):
    # here we are creatng a matrix of size [n+1][capacity+1]. dp[i][j]=> max profit when we have i values and maximum capacity j
    dp=[[None for i in range(capacity+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(capacity+1):
            # if i have 0 items or my capacity is 0 then my profit would be 0
            if i==0 or j==0:
                dp[i][j]=0
            elif weight[i-1]<=j:
                # 2 choices either we include item or not 
                # value[i-1]=> value of ith element(0 - indexing)
                # dp[i-1][j-weight[i-1]]=> maine ith element le liya. ab bache hue i-1 element with capacity - (us element ka wieght jo maine liya) ka knapsack
                #dp[i-1][j]=> maine ith element nahi le liya. ab bache hue i-1 element with capacity ka knapsack
                dp[i][j]= max( ( value[i-1]+dp[i-1][j-weight[i-1]] ) , dp[i-1][j] )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]
 
 



if __name__=='__main__':
    print( knapsack_rec( [10,20,30] , [60,100,120] , 50 , 3 ) )
    print( knapsack_dp( [10,20,30] , [60,100,120] , 50 , 3 ))
      