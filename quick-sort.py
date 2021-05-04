def partition(arr,low,high):
    pivot= arr[low]
    i=low+1
    j=high-1
    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quicksort(arr,low,high):
    if low<high:
        partitioning_point= partition(arr,low,high)
        quicksort(arr,low,partitioning_point-1)
        quicksort(arr,partitioning_point+1,high)
if __name__=='__main__':
    arr=[1,4,8,16,23,15,15,23]
    quicksort(arr,0,len(arr)-1)
    print(arr)