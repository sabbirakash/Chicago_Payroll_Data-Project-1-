#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


pay = pd.read_csv(r"G:\Data Science Project\Resources\2023-11-16-Capstone Project-1 Data Analysis using Pandas\Capstone Project-1 Data Analysis using Pandas\City_of_Chicago_Payroll_Data.csv")
pay


# In[3]:


pay.info()


# In[4]:


pay.isna().sum()


# In[5]:


pay.describe()


# In[6]:


pay.describe(include="all")


# 1.	What are the maximum, minimum and average Typical Hours? (use 'Typical Hours' column)

# In[7]:


pay["Typical Hours"].max()


# In[8]:


pay["Typical Hours"].min()


# In[9]:


pay["Typical Hours"].mean()


# In[10]:


print("Max Typical Hour are :", pay["Typical Hours"].max())
print("Min Typical Hour are :", pay["Typical Hours"].min())
print("Average Typical Hour are :", pay["Typical Hours"].mean())


# 2.	How many employees are on salary and how many are working on hourly basis?

# In[11]:


pay["Salary or Hourly"].value_counts()


# In[12]:


pay.groupby("Salary or Hourly").count()[["Name"]]


# 3.	Which department has maximum no of employees?

# In[13]:


pay.Department.value_counts().head(1)


# In[14]:


pay.groupby("Department").count()[["Name"]].idxmax()


# In[15]:


pay.groupby("Department").count().sort_values(by = "Name", ascending = False).head(1)[["Name"]]


# 4.	How many employees are on Salary and how many are on Hourly in the Police department?

# In[16]:


a = pay[pay.Department == "POLICE"]
a


# In[17]:


a.groupby("Salary or Hourly").count()[["Name"]]


# In[18]:


pay[pay.Department == "POLICE"]["Salary or Hourly"].value_counts()


# 5.	What are the mean, max and min salaries?

# In[19]:


pay["Salary"] = pay["Annual Salary"].str.replace("$", "").astype(float)


# In[20]:


pay["Salary"].info()


# In[21]:


print("Max Salary is :", pay.Salary.max())
print("Min Salary is :", pay.Salary.min())
print("Avg Salary is :", pay.Salary.mean())


# 6.	Find an employee who has the maximum salary

# In[22]:


pay[pay["Salary"]==pay.Salary.max()]


# In[23]:


pay.loc[pay["Salary"].idxmax()]


# 7.	What are the mean, max and min Hourly Rate?

# In[24]:


pay["H_rate"]=pay["Hourly Rate"].str.replace("$", "").astype(float)


# In[25]:


print("Max Salary of Hourly Rate is :",pay["H_rate"].max())
print("Min Salary of Hourly Rate is :",pay["H_rate"].min())
print("Avg Salary of Hourly Rate is :",pay["H_rate"].mean())


# 8.	How many employees are getting max Hourly Rate?

# In[26]:


pay[pay["H_rate"] == pay["H_rate"].max()].count()["Name"]


# 9.	Who is getting max Hourly Rate?

# In[27]:


pay[pay["H_rate"] == pay["H_rate"].max()]


# In[28]:


pay.iloc[[pay["H_rate"].idxmax()]]


# 10.	How many employees are earning less than the average Hourly Rate?

# In[29]:


pay[pay["H_rate"] < pay["H_rate"].mean()]["Name"].count()


# 11.	How many employees are paid hourly and they have full-time job?

# In[30]:


pay[(pay["Full or Part-Time"]=="F") & (pay["Salary or Hourly"] == "Hourly")]


# In[31]:


pay[(pay["Full or Part-Time"]=="F") & (pay["Salary or Hourly"] == "Hourly")].count()["Name"]


# 12.	Find the full-time employees who are working at hourly rate of $10.00?

# In[32]:


pay[pay["Hourly Rate"] == "$10.00"]


# In[33]:


pay[pay["Full or Part-Time"] == "F"]


# In[34]:


pay[(pay["Hourly Rate"] == "$10.00") & (pay["Full or Part-Time"] == "F")]


# 13.	How many unique Job Titles are there in the data?

# In[35]:


pay["Job Titles"].unique()


# In[36]:


pay["Job Titles"].nunique()


# 14.	What was the average Salary of the employees in each department?

# In[37]:


pay["Salary"].mean()


# In[38]:


pay.groupby("Department")["Salary"].mean()


# 15.	What is the job title of 'AGAR, BULENT B'? 

# In[39]:


pay[pay["Name"]=="AGAR,  BULENT B"]["Job Titles"]


# 16.	What are the top most common job titles?

# In[40]:


pay["Job Titles"].value_counts().head(1)


# 17.	How many people have the word 'officer' in their job title? (This is pretty tricky)

# In[41]:


def find_string(title):
    if "OFFICER" in title.upper():
        return True
    else:
        return False


# In[42]:


pay["Job Titles"].apply(find_string)


# In[43]:


pay["Job Titles"].apply(find_string).sum()


# In[44]:


sum(pay["Job Titles"].apply(find_string))

