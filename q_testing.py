import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
from ans_generate import multi
from init import *
import random

### 題目關聯回測 ###
# Build Data
q = [3, 6, 9, 12, 15, 18, 21, 24] #questions related to dim
q = [2+i*3 for i in range(8)]
a = [1,0]
n=len(q)
b=a
while n>1:
    # print(pd.DataFrame(a))
    # print()
    a=multi(a,b)
    n-=1

com = pd.DataFrame(a)
del(a)

# fixed_ans = np.ones((24-len(q)), dtype=np.int)
seed = 97
random.seed(seed)
fixed_ans = np.array(random.choices(range(0, 2), k=(24-len(q))))
dt_ans = pd.DataFrame(np.tile(fixed_ans, len(com)).reshape(-1, 24-len(q)))


for i in range(len(q)):
    dt_ans.insert(loc=(q[i]-1), column=str(q[i]-1), value=com.iloc[:,i])


colnames = [str(i) for i in range(1, 25)] # rename question index
dt_ans.columns = colnames 
dt_ans['ADV'] = 0
dt_ans['INT'] = 0
dt_ans['UNC'] = 0


# Parse Results
xtoken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzI1Mjg3MDgsImV4cCI6MTYzMjYxNTEwOCwiZW1haWwiOiJhbm9uXzY0NDM0NzIxMkBtYXJrZXRpbmcuY29tIiwiaWQiOjI0MjIwNSwidHlwZSI6InRva2VuIiwiYWNjb3VudCI6Im1hcmtldGluZyIsImtleSI6ImZmYTBiZTNjODAzMDNhMjRhZDY0MjEwZTUyMmRlOTY2MjhkZThiYzIiLCJzZXNzaW9uX2tleSI6ImVhMzQ2NzczZGVmOGNiMDMzNTIxYzk0NzY0N2UwMzc5NmQ1ZDc2MjIifQ.YHdS6Shox-kRALIjIQaGYO2ewrB-j8J2gw7H-_pjl_ISm06Pad1Psnc9YMdj6MRdQoaiLtMd7o3FYwhTdq31lya4fUi7x9teUU27uUFue80C4GnQsWgKaqDJWaxsp4KbBhvTCfPmZyTwfL5fEu0FX2Ahw9WAuzfILY7iVrEc0RrYnW5qOxvNY0DsBtdX9Nw_w8StvMAOrNEcv6d4rlKNEobDmCz43LNbtG3d96kPWZ4zddJvV09y9X8d8Efddlu4iDQnB6ltNWWfJEuuNDSByyz1KW4gzV6jXmuL07dq44TMp7WdQWNb2bmqdKLQGnQUgpf52iH0DBjNVf97j76owpNguJRo5vV8t06OQ6ZYrF4bmg9_4YSCkZ8dPgKI8dzyCdjWVgIfAVJ0B0o4VQS_r1QSpclvxag4PPykpslTM76qali2RTY5ZjRfnFQDglQXxxSdmw04Mg18lDROWGDpRdA9fBMi2EYGZt0MlhSF4WbMq-qdQv63OL86PW8L4vEW7hU7R0VjSAP3I4d1hurrhXIe7whbQhFdnup1nqU7W0Ypl1PHCClrpEJfmBgQZ0oYkiDXT25JN_ooTjzWEIn_PWoM8KzWscDFJ13IIPtZWyIPahHiaDq6eCCBdWaUUDAoagU3MyBQX7etGTUbVe9nnUqQ5O0m5bKEjCiE8D_2KYE"
result = tokenCheck(xtoken)
token = result['token']
uid = result['uid']
qtoken = result['qtoken']
result_key = result['vid']

save_path = '../parse_result_INT_random'+str(seed)+'.csv'

for i in range(len(dt_ans)):
    if (i%50==0 & (i!=0)):
        result = tokenCheck(xtoken)
        dt_ans.head(i).to_csv(save_path)
    
    if((i%100==0) & (i!=0)):
        print('Sleeping...')
        time.sleep(100)

    try:
        print('Progress: '+str(i)+'/'+str(len(dt_ans)))
        v = dt_ans.iloc[i,:24]
        ans = ansTrans(v, uid, result_key)                                        
        submmit(token, qtoken, ans, uid)
        s = score(token, uid)
        dt_ans.iloc[i, 24] = s[2]
        dt_ans.iloc[i, 25] = s[0]
        dt_ans.iloc[i, 26] = s[1]

        print('')
        
    except:
        print('token failed')

dt_ans.to_csv(save_path)

# # Analysis: Decision Tree 
# dim = ['INT'] # ADV, INT, UNC
# X = dt_ans.iloc[:,0:24]
# y = dt_ans[dim]
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)


# dtree = DecisionTreeClassifier()
# dtree.fit(X_train,y_train)
# pred = dtree.predict(X_test)
# print(classification_report(y_test,pred))
# print(confusion_matrix(y_test,pred))
# print(tree.export_text(dtree))

# tree.plot_tree(dtree, feature_names=dt_ans.columns[:25],
#                 class_names=sorted(dt_ans[dim].value_counts().index),
#                 filled=True, rounded=True)
