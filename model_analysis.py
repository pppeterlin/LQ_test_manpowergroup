import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import fnmatch
# dt = pd.read_excel('../test.xlsx', 幾)


k = 0
ind_start = 2**(17+k)
path = '../parse_result_'+str(ind_start)+'.csv'
dt = pd.read_csv(path)

for i in range(1, 7):
    dt1 = ind_start = 2**(17+i)
    path = '../parse_result_'+str(ind_start)+'.csv'
    dt1 = pd.read_csv(path)
    dt = pd.concat([dt, dt1])

dt1 = pd.read_csv('../parse_7750.csv')
dt = pd.concat([dt, dt1])

# dt = pd.read_csv('../parse_831.csv')
# dt = pd.read_csv('../parse_result_131072.csv')




dt = dt[dt.ADV!='0'] # remove 0
dt.drop(dt.columns[0], axis=1, inplace=True) # drop first column
colnames = [str(i) for i in range(1, 25)] # rename question index
colnames.extend(['ADV', 'INT', 'UNC'])
dt.columns = colnames 

# Decision Tree
from sklearn.model_selection import train_test_split
X = dt.iloc[:,0:24]
y = dt['UNC']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

pred = dtree.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

from sklearn import tree
print(tree.export_text(dtree))

tree.plot_tree(dtree, feature_names=dt.columns[:25],
                class_names=sorted(dt.UNC.value_counts().index),
                filled=True, rounded=True)


# sum of T
M = pd.DataFrame()
M['a_E'] = dt[dt['a']=='E'].iloc[:,:-3].sum(axis=0, skipna=False)
M['a_T'] = dt[dt['a']=='T'].iloc[:,:-3].sum(axis=0, skipna=False)
M['a_P'] = dt[dt['a']=='P'].iloc[:,:-3].sum(axis=0, skipna=False)

M['b_T'] = dt[dt['b']=='T'].iloc[:,:-3].sum(axis=0, skipna=False)
M['b_D'] = dt[dt['b']=='T'].iloc[:,:-3].sum(axis=0, skipna=False)
# b_S = dt[dt['a']=='S'].iloc[:,0:24].sum(axis=1)

M['c_I'] = dt[dt['c']=='I'].iloc[:,:-3].sum(axis=0, skipna=False)
M['c_T'] = dt[dt['c']=='T'].iloc[:,:-3].sum(axis=0, skipna=False)
M['c_F'] = dt[dt['c']=='F'].iloc[:,:-3].sum(axis=0, skipna=False)
M



X_test = dt1.iloc[:,:24]
y_test = dt1['INT']

pred = dtree.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

from sklearn import tree
print(tree.export_text(dtree))




from sklearn.model_selection import train_test_split
X = dt1.iloc[:,0:24]
y = dt1['INT']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

pred = dtree.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

from sklearn import tree
print(tree.export_text(dtree))



i = 100
if ((i%50==0) & (i!=0)):
    print('check')
else:
    print('pass')


_adv = [3, 6, 12, 15, 18, 21, 24]
_int = [2, 5, 14, 17, 20, 23]
_unc = [1, 4, 7, 13, 16, 19, 22]
set(range(1, 15)) - set(_adv+_int+_unc)




### 題目關聯回測 ###
q = ['9', '10']
dt_ans = pd.DataFrame(np.ones(24*2**len(q), dtype=np.int).reshape(-1, 24))
dt_ans = pd.concat([dt_ans, pd.DataFrame(np.zeros(24*2**len(q), np.int).reshape(-1, 24))])

colnames = [str(i) for i in range(1, 25)] # rename question index
dt_ans.columns = colnames 
dt_ans['ADV'] = 0
dt_ans['INT'] = 0
dt_ans['UNC'] = 0

from ans_generate import multi
a = [1,0]
n=len(q)
b=a
while n>1:
    # print(pd.DataFrame(a))
    # print()
    a=multi(a,b)
    n-=1

com = pd.DataFrame(a)
com = pd.concat([com, com])
dt_ans[q] = com[::]


# Parse Results
from init import *
xtoken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzE4NjAzMjYsImV4cCI6MTYzMTk0NjcyNiwiZW1haWwiOiJhbm9uXzEwNDU0ODI0MTlAbWFya2V0aW5nLmNvbSIsImlkIjoyNDAxNTMsInR5cGUiOiJ0b2tlbiIsImFjY291bnQiOiJtYXJrZXRpbmciLCJrZXkiOiI2NjI0NTQ5NjkyNWFjMWE4MmRjMzAzYTgxNTQxNDlkYjQyZWU0NmRiIiwic2Vzc2lvbl9rZXkiOiI0M2M4NTQxMjcwMzU1YzgxZjMyNzYxNjNjNTI2ODNlYzM5Njg0ZGMzIn0.S7HWQIWkByse_R8zRCk7xxv5vdTEGCFTrr3YTSkoS1LEq05HDKOfL7w43IrvLKIglBErey4hYMMfV8AKe3BvHA9xkwjdgLtkix37E-euD6jHt6wfWBxp08fDg6si7qQgWl_Atz-9zqOeC-o3SIsNrf0iDhh1pDtHKEUzlw0nUN6hso8NOYExY-1Xj2AOuoZ3RmhUT-x4SMm1W-BY3geXrz9DZn4DS5j6941UOiu0FZchos6JKXjoeq1xdlFzcQnytxMjJCjwkdYrzy9bmhlQE6TFY7sUjWDtEXjziLBUTJU3WQzU6460GZ2syV4b1C7HGhuH8m1qkLSk2VPZ3w5zwY3kEXYn1-WESTUX_irLViWAOiuLNp6Z43jQrtPN4_TJxYGzfVryg2LZrFjUDmLoBp0bPYvTXy8efaa6RsUOWByHt5_JQQqU3jHPUkSo0xezWNS96vapvUTEHGALDuh0DStELO4XbpdSq5Y2J-htQ0yJmnMu127ega2wRqWu0U2fvF1xyrNXVLmkdjfG9wPZ3nqU1Krs7FVf3BwiHivoNq_ylNzHlwF2C1cDd-zC-KII5cLOi_z7-G2SpYzJu--5ZaSif4yteWo8pQkjJ5vI_2kbW_bVQ7U-4MCdJKKJpxbrGc1VzNsr0x6R4FvJTunZuNBBLtMSnh4N3xyip_Wk5mE"
result = tokenCheck(xtoken)
token = result['token']
uid = result['uid']
qtoken = result['qtoken']
result_key = result['vid']

for i in range(len(dt_ans)):
     
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

# Analysis: Decision Tree 
dim = ['INT'] # ADV, INT, UNC
X = dt_ans.iloc[:,0:24]
y = dt_ans[dim]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)


dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)
pred = dtree.predict(X_test)
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))
print(tree.export_text(dtree))

tree.plot_tree(dtree, feature_names=dt_ans.columns[:25],
                class_names=sorted(dt_ans[dim].value_counts().index),
                filled=True, rounded=True)





# Combine random data sets
f_list = []
for f in os.listdir('../'):
    if fnmatch.fnmatch(f, '*_random*'):
        # print(f)
        df = pd.read_csv('../'+f)
        f_list.append(df)
dt = pd.concat(f_list)

# analysis pattern: ADV
dim = []
for i in range(int(len(dt)/256)):
    dim.append(dt.iloc[i*256:(i+1)*256]['INT'])

dim = pd.DataFrame(dim).T
dim[dim.apply(pd.Series.nunique, axis=1)==1]
dim[dim.apply(pd.Series.nunique, axis=1)!=1]