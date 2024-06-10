import pandas as pd

df = pd.DataFrame({
  "Name": ["Chicken", "Barbed Wire", "Donut", "QT", "Darth Sith", "Leopard"],
  "Age": [2, 125, 5, 25, 86, 46],
  "City": ["London", "Hong Kong", "Dunkin", "Stockholm", "Mars", "Djibouti"]
})

#print(df.head())

#print(df.shape)

#print(df["Name"])

#print(df["Age"].max()

#print(type(df["Age"]))

#print(df["Age"].shape)

#print(df.describe())

v = pd.read_csv("./titanic.csv")

#print(v.head())

#print(v.info())

#print(v.dtypes)

nameandage = v[["Name","Age"]]

#print(nameandage)

class2 = v[v["Pclass"].isin([2,3])]

#print(class2[["Name","Pclass"]].head())

malefirstclass = v[(v["Sex"] == "male") & (v["Pclass"] == 1)]
#print(malefirstclass)

print(malefirstclass["Fare"].mean())