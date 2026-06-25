import pandas as pd

df = pd.read_csv(
    r"C:\Users\ABC\OneDrive\Desktop\HR Analytics Dashboard\data\raw\WA_Fn-UseC_-HR-Employee-Attrition.csv",
    encoding='latin1'
)

df.columns = df.columns.str.replace('ï»¿', '', regex=False)

print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n")

print("=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns.tolist())

print("\n")

print("=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n")

print("=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)
print(df.duplicated().sum())

print("\n")

df.drop(
    columns=[
        'EmployeeCount',
        'EmployeeNumber',
        'Over18',
        'StandardHours'
    ],
    inplace=True
)

df['Attrition_Flag'] = df['Attrition'].map({
    'Yes': 1,
    'No': 0
})

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n")

total_employees = len(df)

print("=" * 50)
print("TOTAL EMPLOYEES")
print("=" * 50)
print(total_employees)

print("\n")

print("=" * 50)
print("ATTRITION COUNT")
print("=" * 50)
print(df['Attrition'].value_counts())

print("\n")

attrition_count = len(df[df['Attrition'] == 'Yes'])

attrition_rate = round(
    (attrition_count / total_employees) * 100,
    2
)

print("=" * 50)
print("ATTRITION RATE")
print("=" * 50)
print(f"{attrition_rate}%")

print("\n")

# Department Wise Attrition

print("=" * 50)
print("DEPARTMENT WISE ATTRITION")
print("=" * 50)

dept_attrition = pd.crosstab(
    df['Department'],
    df['Attrition']
)

print(dept_attrition)

print("\n")

# Gender Wise Attrition

print("=" * 50)
print("GENDER WISE ATTRITION")
print("=" * 50)

gender_attrition = pd.crosstab(
    df['Gender'],
    df['Attrition']
)

print(gender_attrition)

print("\n")

# Job Role Wise Attrition

print("=" * 50)
print("JOB ROLE WISE ATTRITION")
print("=" * 50)

jobrole_attrition = pd.crosstab(
    df['JobRole'],
    df['Attrition']
)

print(jobrole_attrition)

print("\n")

# Overtime Wise Attrition

print("=" * 50)
print("OVERTIME VS ATTRITION")
print("=" * 50)

overtime_attrition = pd.crosstab(
    df['OverTime'],
    df['Attrition']
)

print(overtime_attrition)

print("\n")


# Marital Status Attrition

print("=" * 50)
print("MARITAL STATUS ATTRITION")
print("=" * 50)

marital_attrition = pd.crosstab(
    df['MaritalStatus'],
    df['Attrition']
)

print(marital_attrition)

print("\n")

# Average Age

avg_age = round(df['Age'].mean(), 2)

print("=" * 50)
print("AVERAGE AGE")
print("=" * 50)
print(avg_age)

print("\n")

# Average Monthly Income

avg_income = round(df['MonthlyIncome'].mean(), 2)

print("=" * 50)
print("AVERAGE MONTHLY INCOME")
print("=" * 50)
print(avg_income)

print("\n")

# Save Cleaned Dataset

output_path = r"C:\Users\ABC\OneDrive\Desktop\HR Analytics Dashboard\data\processed\HR_Employee_Cleaned.csv"

df.to_csv(output_path, index=False)

print("=" * 50)
print("CLEANED DATASET SAVED")
print("=" * 50)
print(output_path)