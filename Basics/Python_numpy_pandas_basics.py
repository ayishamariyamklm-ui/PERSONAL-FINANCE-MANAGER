# ============================================
# NumPy & Pandas Basics
# ============================================

import numpy as np
import pandas as pd 

# -------- NumPy --------

# Create array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

# Mathematical operations
print("Array + 2:", arr + 2)
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))


# -------- Pandas --------

# Create DataFrame
data = {
    "Name": ["Ayisha", "Sara", "Ameen"],
    "Age": [22, 21, 23],
    "Marks": [85, 78, 90]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# Access column
print("\nMarks Column:")
print(df["Marks"])

# Simple filtering
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])


print("\n--------------------------------------------") 


print("END OF PYTHON NUMPY PANDAS BASICS")