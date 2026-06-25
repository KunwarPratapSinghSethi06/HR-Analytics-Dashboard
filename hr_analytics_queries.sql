CREATE DATABASE hr_analytics;
USE hr_analytics;

#Total Employees
SELECT COUNT(*) AS Total_Employees
FROM hr_Employee;

#Attrition Count
SELECT Attrition, COUNT(*) AS Employee_Count
FROM hr_employee
GROUP BY Attrition;

#Attrition Rate
SELECT
ROUND(
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
/ COUNT(*),
2
) AS Attrition_Rate
FROM hr_employee;

#Department-wise Attrition
SELECT
Department,
COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_employee
GROUP BY Department
ORDER BY Attrition_Count DESC;

#Job Role-wise Attrition
SELECT
JobRole,
COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_employee
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

#Gender-wise Attrition
SELECT
Gender,
COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_employee
GROUP BY Gender;

#Overtime Analysis
SELECT
OverTime,
COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_employee
GROUP BY OverTime;

#Marital Status Analysis
SELECT
MaritalStatus,
COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_employee
GROUP BY MaritalStatus;

#Average Salary by Department
SELECT
Department,
ROUND(AVG(MonthlyIncome),2) AS Avg_Salary
FROM hr_employee
GROUP BY Department
ORDER BY Avg_Salary DESC;

#Average Age by Department
SELECT
Department,
ROUND(AVG(Age),2) AS Avg_Age
FROM hr_employee
GROUP BY Department;

#Top 10 Highest Paid Employees
SELECT
JobRole,
Department,
MonthlyIncome
FROM hr_employee
ORDER BY MonthlyIncome DESC
LIMIT 10;

#Employee Satisfaction Analysis
SELECT
JobSatisfaction,
COUNT(*) AS Employees
FROM hr_employee
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

#Attrition by Age Group
SELECT
CASE
    WHEN Age < 30 THEN 'Under 30'
    WHEN Age BETWEEN 30 AND 40 THEN '30-40'
    WHEN Age BETWEEN 41 AND 50 THEN '41-50'
    ELSE '50+'
END AS Age_Group,

COUNT(*) AS Employees,

SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count

FROM hr_employee

GROUP BY Age_Group;