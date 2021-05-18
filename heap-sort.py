def heapify(arr,i,n):
    largest= i
    left= (2*i)+1
    right= (2*i)+2
    if left<n and arr[left]>arr[i]:
        largest= left
    if right<n and arr[right]>arr[largest]:
        largest= right
    if largest!=i:
        arr[i],arr[largest]= arr[largest],arr[i]
        heapify(arr,largest,n)
def heap_sort(arr):
    n= len(arr)
    for i in range(n//2-1,-1,-1):  # n//2-1 th node is the last node with child
        heapify(arr,i,n)
    # now heapifying all nodes from right to left
    for i in range(n-1,0,-1):
        arr[0],arr[i]= arr[i],arr[0]
        heapify(arr,0,i)
if __name__=='__main__':
    arr=[1,4,8,16,23,15,15,23]
    heap_sort(arr)
    print(arr)