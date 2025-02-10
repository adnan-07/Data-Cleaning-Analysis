import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel("raw_data.xlsx")

# Fill missing values in "Salary" with the average salary
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Fill missing values in "Age" with the median age
df["Age"].fillna(df["Age"].median(), inplace=True)

# Convert "Joining Date" column to datetime format
df["Joining Date"] = pd.to_datetime(df["Joining Date"])

# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Save the cleaned data to a new Excel file
df.to_excel("cleaned_data.xlsx", index=False)

# 📊 Generate a Salary Distribution Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Salary"], color="skyblue")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Salary Distribution of Employees")
plt.xticks(rotation=45)
plt.savefig("salary_distribution.png")  # Save the graph as an image
plt.show()

print("✅ Data cleaning completed. Reports saved as 'cleaned_data.xlsx' and 'salary_distribution.png'.")
