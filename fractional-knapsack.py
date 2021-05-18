def bubble(weight,value,value_per_weight):
    n=len(value_per_weight)
    for i in range(n-1):
        for j in range(n-1-i):  
            if value_per_weight[j]<value_per_weight[j+1]:
                value_per_weight[j],value_per_weight[j+1]=value_per_weight[j+1],value_per_weight[j]
                weight[j],weight[j+1]=weight[j+1],weight[j]
                value[j],value[j+1]=value[j+1],value[j]

def frac_knap(weight,value,capacity,n):
    ans=0.0  #storing max profit or vallue
    value_per_weight=[]
    for i in range(n):
        value_per_weight.append(value[i]/weight[i])
    #sorting in desc order according to value_per_weight
    bubble(weight,value,value_per_weight)
    for i in range(n):
        # if the wieght of item<=curr
        if weight[i]<=capacity:
            capacity-= weight[i]
            ans+= float(value[i])
        else:
            ans+= value_per_weight[i]*float(capacity)
    return ans
if __name__=='__main__':
    weight=[10,20,30]
    value=[60,100,120]
    capacity=50
    ans= frac_knap(weight,value,capacity,3)
    print(ans)