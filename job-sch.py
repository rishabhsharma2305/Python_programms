class job:
    def __init__(self,id,deadline,profit):
        self.id= id
        self.profit=profit
        self.deadline=deadline

def job_sched(jobs,t):
    # sorting according to deadline
    n=len(jobs)
    for i in range(n-1):
        for j in range(n-1-i):
            if jobs[j].deadline<jobs[j+1].deadline:
                jobs[j],jobs[j+1]=jobs[j+1],jobs[j]
    res=[-1]*t
    slot=[False]*t  # initially every slot is free
    # for itreating ove jobs
    for i in range(n): 
        # for itrating over slots
        # in this loop we will move backwards checking for maximum slot.(job with deadline 3 should be schd at 3 and not 1 or 2 if possible)
        # reason for min is if job has dd of 3 then there is no sense to itrate from 5
        for j in range(min(t-1,jobs[i].deadline-1),-1,-1):# dd-1 because index 2 represent slot 2 to 3
            print(j,end=" ")
            if slot[j]==False:
                res[j]=jobs[i]
                slot[j]=True # book the slot
                break
    return res
if __name__=='__main__':
    j1= job(1,2,100)
    j2= job(2,1,19)
    j3= job(3,2,27)
    j4= job(4,1,25)
    j5= job(5,3,15)
    ans= job_sched([j1,j2,j3,j4,j5],3)
    print()
    for i in range(3):
        print(ans[i].id,end=" ")
    max_profit=0
    for i in range(3):
        max_profit+= ans[i].profit
    print("max profit=",max_profit)
    print