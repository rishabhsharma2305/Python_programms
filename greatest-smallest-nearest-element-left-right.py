def gner(arr):
    stack= []
    res= []
    for i in range(len(arr)-1,-1,-1):
        while( len(stack)!=0 and stack[-1]<=arr[i] ):
            stack.pop()
        if(len(stack)==0):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    res.reverse()
    return res

def sner(arr):
    stack= []
    res= []
    for i in range(len(arr)-1,-1,-1):
        while( len(stack)!=0 and stack[-1]>=arr[i] ):
            stack.pop()
        if(len(stack)==0):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    res.reverse()
    return res

def gnel(arr):
    stack= []
    res= []
    for i in range(len(arr)):
        while( len(stack)!=0 and stack[-1]<=arr[i] ):
            stack.pop()
        if(len(stack)==0):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    # res.reverse()
    return res

def snel(arr):
    stack= []
    res= []
    for i in range(len(arr)):
        while( len(stack)!=0 and stack[-1]>=arr[i] ):
            stack.pop()
        if(len(stack)==0):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    # res.reverse()
    return res

if __name__ == '__main__':
    print("gner\n")
    res= gner([5,6,3,2,9,4,7,5])
    for i in res:
        print(i,end=" ")
    print()
    print("sner\n")
    res= sner([5,6,3,2,9,4,7,5])
    for i in res:
        print(i,end=" ")
    print()
    print("gnel\n")
    res= gnel([5,6,3,2,9,4,7,5])
    for i in res:
        print(i,end=" ")
    print()
    print("snel\n")
    res= snel([5,6,3,2,9,4,7,5])
    for i in res:
        print(i,end=" ")
    print()