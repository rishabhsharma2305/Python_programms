def merge_sort(arr,low,mid,high):
    i=k=low
    j=mid+1
    temp=[None]*(high-low+1)
    print("low= ",low)
    print("mid= ",mid)
    print("high= ",high)
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            j+=1
            k+=1
    while i<mid+1:
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<high+1:
        temp[k]=arr[j]
        k+=1
        j+=1
    for elements in range(low,high+1):
        arr[elements]= temp[elements]

def merge(arr,low,high):
    if low<high:
        mid= (low+high)//2
        merge(arr,low,mid)
        merge(arr,mid+1,high)
        merge_sort(arr,low,mid,high)
if __name__=='__main__':
    arr=[81,4,16,23]
    merge(arr,0,len(arr)-1)
    print(arr)