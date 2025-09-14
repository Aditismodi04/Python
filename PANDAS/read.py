import pandas as pd

# data = {
#     "name":["aditi","purv","aayushi","riddhi","shaily","vaibhav"],
#     "age":[21,20,21,24,27,25],
#     "salary":[10000,15000,12000,21000,8000,13000],
#     "score" :[50,67,37,89,32,45]
#     }
# df= pd.DataFrame(data)
# print(df)
# print("-------------------------")
# df.to_csv("mydata.csv",index=False,encoding="latin1")
# # print(df[(df["salary"]>12000 )&(df["score"]>55) ])
# df["city"] = ["surat","bombay","baroda","ahmd","delhi","pune"]
# print(df)
# df.insert(1,"grade",["A","B","C","D","E","F"])
# print(df)
# df.to_csv("mydata.csv",index=False,encoding="latin1")
# df.loc[0,"salary"] =25000
# print(df)
# df["salary"] = df["salary"]*1.5
# print(df)
# df.drop(columns = ["grade","city"] ,inplace=True)
# print(df)
# data = {
#     "name":["aditi",None,"aayushi","riddhi","shaily","vaibhav"],
#     "age":[21,None,21,24,27,25],
#     "salary":[10000,None,12000,21000,8000,13000],
#     "score" :[50,67,None,89,32,45]
#     }
# df = pd.DataFrame(data)
# print(df.isnull().sum())
# df.dropna(axis =0,inplace=True)
# print(df)
# df.fillna(0,inplace=True)
# df["age"].fillna(df["age"].mean(),inplace=True) 
# df["score"].fillna(df["score"].mean(),inplace=True) 
# print(df)
# data = {
#     "values":[10,20,10,50,None],
#     "time": [1,2,None,None,9]
# }
# df = pd.DataFrame(data)
# print(df)
# print()
# df["values"] = df["values"].interpolate(method="linear")
# df["time"] = df["time"].interpolate(method="linear")
# print(df)
# print()
# df.sort_values(by=["values","time"] ,  ascending=[True,True] ,inplace=True)
# print(df)
# avg = df["values"].median ()
# print(avg)
# data = {
#     "name":["aditi","purv","aayushi","riddhi","shaily","vaibhav"],
#     "age":[21,20,21,24,27,25],
#     "salary":[10000,15000,12000,21000,8000,13000],
#     "score" :[50,67,37,89,32,45]
#     }
# df = pd.DataFrame(data)
# print(df)
# print()
# group = df.groupby("age")["salary"].sum()
# print(group)
# grouped = df.groupby(["age","name"])["salary"].sum()
# print(grouped)

c1 = {
    "id" : [1,2,3],
    "Amount" :[1000,3400,2367]
}
df = pd.DataFrame(c1)

c2 = {
    "id" : [2,3,4],
    "name" : ['aditi' ,"purv", "shaily"]
}
df1 = pd.DataFrame(c2)

df_merged = pd.merge(df,df1,on= "id",how="right")
print(df_merged)
df_concet = pd.concat([df,df1],axis=0,ignore_index=True)
print(df_concet)