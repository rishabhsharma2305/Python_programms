# need to find both nsel & nser 

#for getting list of indexes of nsel
def index_of_smallest_left(arr):
    index= []                    #for storing the index of nearest smallest element
    stack= []                    # stack will store tupple of (element,index)
    for i in range(len(arr)):
        while len(stack)!=0 and stack[-1][0]>=arr[i]:
            stack.pop()
        if len(stack)==0:
            index.append(-1)
        else:
            index.append(stack[-1][1])  #stack[-1][1]----->index of element at top
        stack.append( (arr[i],i) )      #appending the tupple
    
    return index

#for getting list of indexes of nser
def index_of_smallest_right(arr):
    index= []
    stack= []
    for i in range(len(arr)-1,-1,-1):
        while len(stack)!=0 and stack[-1][0]>=arr[i]:
            stack.pop()
        if len(stack)==0:
            index.append(-1)
        else:
            index.append(stack[-1][1])
        stack.append( (arr[i],i) )
    index.reverse()
    return index

def max_area_hist(arr):
    right= index_of_smallest_right(arr)
    left= index_of_smallest_left(arr)
    width= []
    res= []

    # usually we assume -1 if no index found but in case of right side we will assume index after last index i.e length
    for i in range(len(right)):
        if right[i]==-1:
            right[i]=len(arr)
    # for getting width
    for i in range(len(right)):
        width.append(right[i]-left[i]-1)
    #finding area
    for i in range(len(arr)):
        res.append(arr[i]*width[i])
    return max(res)
if __name__== '__main__':
    print(max_area_hist([1,8,6,2,5,4,8,3,7]))
    print()