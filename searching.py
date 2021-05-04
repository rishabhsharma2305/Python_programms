def linear_search(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return -1
def binary_search(arr,n):
    arr.sort()
    beg=0
    end=len(arr)-1
    while beg<=end:
        mid=(beg+end)//2
        if arr[mid]==n:
            return mid
        elif n>arr[mid]:
            beg=mid+1
        else:
            end=mid-1
    return -1
if __name__=='__main__':
    arr=[2,5,4,3,1,56,76]
    print(linear_search(arr,56))
    print(binary_search(arr,569))