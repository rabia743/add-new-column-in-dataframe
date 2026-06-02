# Add New Column in Pandas DataFrame

## Description

This Python program demonstrates how to create a Pandas DataFrame and add a new column to it.

## Features

* Create a DataFrame using a dictionary
* Set custom index names
* Add a new column named **Salary**
* Display the updated DataFrame

## Code Example

```python
import pandas as pd
data = {"Name":["Ali","Raza"],
        "Age":[20,21]}
s = pd.DataFrame(data,index=["Employee no 1","Employee no 2"])
print(s)

# add new column
s["Salary"] = [50000,40000]
print(s)
```

## Output

The program first prints the original DataFrame and then prints the updated DataFrame after adding the Salary column.

## Concept Used

**Add New Column in DataFrame:**
A new column is added to store additional information by assigning values to a new column name.

