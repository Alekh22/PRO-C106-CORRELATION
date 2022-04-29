import pandas as pd

data = pd.read_csv("Student Marks vs Days Present.csv")
data2= pd.read_csv("cups of coffee vs hours of sleep.csv")
correlation = data['Marks In Percentage'].corr(data['Days Present'])
correlation2 =data2['Coffee in ml'].corr(data2["sleep in hours"])
print(correlation)
print(correlation2)


