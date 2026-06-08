# adding columns in dataframe
import pandas as pd
data = {"Name":["Ali","Raza"],
        "Age":[20,21]}
s = pd.DataFrame(data,index=["Employee no 1","Employee no 2"])
print(s)
# add new column
s["Salary"] = [50000,40000]
print(s)
