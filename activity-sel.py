# act sel problem
def act_sel_rec(start,finish,n,m,ans):
    # m is the last act scheduled till now. i need to check act after m
    k=m+1
    #skipping all the activities whose finish time>start time of my current act
    while k<n and start[k]<finish[m]:
        k+=1
    if k<n:
        ans.append(k)
        # now scheduled kth act 
        act_sel_rec(start,finish,n,k,ans)
def act_sel_itr(start,finish,n,m,ans):
    for i in range(1,n):
        if start[i]>=finish[m]:
            ans.append(i)
            m=i

if __name__=='__main__':
    start  = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    #0th act is always scheduled as it is with the least finishing time
    ans=[0]
    act_sel_rec(start,finish,len(start),0,ans)
    print(ans)
    ans=[0]
    act_sel_itr(start,finish,len(start),0,ans)
    print(ans)