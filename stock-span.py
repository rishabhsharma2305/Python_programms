def stock_span(cost):
    index= []
    stack= []
    res=[]
    for i in range(len(cost)):
        while len(stack)!=0 and stack[-1][0]<=cost[i]:
            stack.pop()
        if len(stack)==0:
            index.append(-1)
        else:
            index.append(stack[-1][1])
        stack.append( (cost[i],i) )
    for i in range(len(cost)):
        res.append(i-index[i])
    return res
if __name__=='__main__':
    res= stock_span([100,80,60,70,60,75,85])
    for i in res:
        print(i, end=" ")
    print()
