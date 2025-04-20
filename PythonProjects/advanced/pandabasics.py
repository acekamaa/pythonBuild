import pandas as pd

# Create the initial DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Grade': [85, 45, 67]
}

df = pd.DataFrame(data)

# Add 'Passed' column
df['Passed'] = df['Grade'] > 50

# Filter students who passed
passed_students = df[df['Passed']]

print(passed_students)
