def partition(arr,low,high):
    pivot= arr[high]
    i= low-1
    for j in range(low,high+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]= arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        partitioning_point= partition(arr,low,high)
        quicksort(arr,low,partitioning_point-1)
        quicksort(arr,partitioning_point+1,high)
if __name__=='__main__':
    arr=[1,4,8,16,23,15,15,23]
    quicksort(arr,0,len(arr)-1)
    print(arr)