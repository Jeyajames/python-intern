import pandas as pd
import json
a={'name':['janu','abisha','priya'],
   'age':[15,20,22],
   'address':['chennai','kerala','mumbai']}
with open("inf.json",'w') as json_file:
   json.dump(a,json_file)
with open("inf.json") as i:
   a=json.load(i)
df= pd.DataFrame(a)
print(df)   

   
