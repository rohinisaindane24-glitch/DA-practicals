import pandas as pd 
df = pd.DataFrame({ 
"Student_ID": [101, 102, 103, 104], 
"Age": [19, 20, 18, 21], 
"Course": ["Computer", "IT", "Computer", "ENTC"], 
"City": ["Jalgaon", "Pune", "Nashik", "Dhule"], 
"Attendance": [85, 92, 88, 88], 
"Fees": [45000, 50000, 42000, 48000] 
}) 
print("Original Data:\n", df) 
# Data Subsetting 
print("\nStudent (Attendance > 80):\n", df[df["Attendance"] > 80]) 
# Sorting in Ascending Order 
print("\nSorted by Attendance (Ascending):\n") 
print(df.sort_values("Attendance")) 
# Sorting in Descending Order 
print("\nSorted by Attendance (Descending):\n") 
print(df.sort_values("Attendance", ascending=False)) 
# Grouping 
print("\nGrouped (Average Attendance by Course):\n") 
print(df.groupby("Course")["Attendance"].mean()) 
# Statistical Operations 
print("Mean:", df["Attendance"].mean()) 
print("Median:", df["Attendance"].median()) 
print("Mode:", df["Attendance"].mode()) 
print("Min:", df["Attendance"].min()) 