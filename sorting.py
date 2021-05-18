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

def selection(arr):
    swaps=0
    n=len(arr)
    for i in range(n-1):
        min= i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]= arr[min],arr[i]
        swaps+=1
    print("swaps in selection sort =",swaps)
def insertion(arr):
    swaps=0
    n=len(arr)
    for i in range(1,n):
        key= arr[i]
        j=i-1
        while j>=0 and arr[j]>key: 
            arr[j+1]=arr[j]
            j-=1
            swaps+=1
        arr[j+1]=key
    print("swaps in insertion sort =",swaps)
def bubble(arr):
    n=len(arr)
    swaps=0
    for i in range(n-1):
        for j in range(n-1-i):  # here i am assuming that last i elements are sorted because after every swap heaviest element reach to last
            if arr[j]>arr[j+1]:
                temp= arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swaps+=1
    print("swaps in bubble sort =",swaps)

def bubble_best(arr):
    n=len(arr)
    swaps=0
    while True:
        flag=0
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swaps+=1
                flag=i
        n=flag
        if n==0:
            break
    print("swaps in bubble_best sort =",swaps)
if __name__=='__main__':
    arr=[10,1,3,4,5,15,9]
    bubble(arr)
    print(arr)
    arr=[10,1,3,4,5,15,9]
    insertion(arr)
    print(arr)
    arr=[10,1,3,4,5,15,9]
    selection(arr)
    print(arr)
    arr=[10,1,3,4,5,15,9]
    bubble_best(arr)
    print(arr)
    arr=[10,1,3,4,5,15,9]
    heap_sort(arr)
    print(arr)