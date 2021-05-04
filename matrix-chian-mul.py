import sys
def mcm(arr,i,j):
    if i>=j:
        return 0
    minimum= sys.maxsize
    for k in range(i,j):
        temp= mcm(arr,i,k)+mcm(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp<minimum:
            minimum= temp
    return minimum
if __name__=='__main__':
    arr=[40,20,30,10,30]
    print(mcm(arr,1,len(arr)-1))