def multi(a,b):
    r=[]
    for i in a:
        for j in b:
            if isinstance(i,list):
                temp=i[:]
                temp.append(j)
                r.append(temp)
            else:
                r.append([i,j])
    return r

import pandas as pd
import numpy as np
import time
t_start = time.time()

a=[1,0]
m=len(a)
n=24
b=a
while n>1:
    # print(pd.DataFrame(a))
    # print()
    a=multi(a,b)
    n-=1


d= pd.DataFrame(a)
print(time.time() - t_start)
print('done')

d['ADV'] = 0
d['INT'] = 0
d['UNC'] = 0

d.to_csv("/Users/peterlin/Documents/Python/lq_parser/answers.csv")


# 結果[0,1]轉[T,F]
import pandas as pd
dt = pd.read_csv('../結果/LQ_result_UNC.csv')

t = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
ind = list(range(0, 24, 3))
v_True = [e for i, e in enumerate(t) if i in ind]


for i in range(len(dt)):
    value = dt.iloc[i,:]  
    ans = ['T']*len(ind)
    diff = [i-j for i, j in zip(v_True, list(value))]
    for j in range(len(diff)):   
        if(diff[j]):
            ans[j] = 'F'
    dt.iloc[i, 0:len(ind)] = ans

dt.to_csv('../結果/LQ_result_UNC(轉).csv')