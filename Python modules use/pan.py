import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'dob', 'Charlie'],
    'Age': [25, 30, 20],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df_mean_age = df['Age'].mean()   # Mean age
df_sorted = df.sort_values(by='Name')  # Sort by Age

print("DataFrame:\n", df)
print("\nMean Age:", df_mean_age)
print("\nSorted DataFrame by Age:\n", df_sorted)


