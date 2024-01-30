def knapsack(wt,val,cap,i):
    if i==0 or cap==0:
        return 0
    np,p=0,0
    if cap-wt[i]<0:
        np=knapsack(wt,val,cap,i-1)
        return np
    p=val[i]+knapsack(wt,val,cap-wt[i] ,i-1)
    return max(np,p)