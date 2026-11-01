
# Data Science Project
# Git and GitHub Version Control

import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'Name': ['Amit', 'Rahul', 'Sneha', 'Priya', 'Vijay'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 95, 88]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Original Dataset:")
print(df)

# Calculate average marks
average_marks = np.mean(df['Marks'])

print("\nAverage Marks:", average_marks)

# Display students scoring above average
print("\nStudents scoring above average:")
print(df[df['Marks'] > average_marks])

# Project completed
print("\nData Science Project Executed Successfully!")
