#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd


# You must use Pandas to answer the following questions:
# 
#     How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
#     What is the average age of men?
#     What is the percentage of people who have a Bachelor's degree?
#     What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
#     What percentage of people without advanced education make more than 50K?
#     What is the minimum number of hours a person works per week?
#     What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
#     What country has the highest percentage of people that earn >50K and what is that percentage?
#     Identify the most popular occupation for those who earn >50K in India.
# 

# In[19]:


##installation dataframe
  
adult = pd.read_csv(r"C:\Users\yetsu\Downloads\adult.data.csv") 
adult


# In[20]:


print(adult.columns)
print(adult.shape)


# In[21]:


#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

adult['race'].value_counts()


# In[29]:


#  What is the average age of men?
gender = adult.groupby('sex')
men = gender.get_group('Male')

men['age'].mean()


# In[30]:


#What is the percentage of people who have a Bachelor's degree?

adult['education'].value_counts(normalize = True).mul(100)


# In[34]:


#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

advances_education = adult[adult['education'].isin(['Bachelors','Masters','Doctorate'])]

advances_education['salary'].value_counts(normalize = True).mul(100)


# In[38]:


#What percentage of people without advanced education make more than 50K?
non_advances = adult[adult['education'].isin(['HS-grad','Some-college','Assoc-voc','11th','Assoc-acdm', '10th', '7th-8th', 'Prof-school','9th', '12th', '5th-6th',  '1st-4th', 'Preschool' ])]

non_advances['salary'].value_counts(normalize = True).mul(100)


# In[39]:


#What is the minimum number of hours a person works per week?
min(adult['hours-per-week'])


# In[46]:


#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
hour1 = adult[adult['hours-per-week'] == 1]
hour1['salary'].value_counts(normalize = True).mul(100)


# In[51]:


#What country has the highest percentage of people that earn >50K and what is that percentage? France
country = adult.groupby('native-country')
country['salary'].value_counts(normalize = True).mul(100)


# In[55]:


#Identify the most popular occupation for those who earn >50K in India.

india = adult[adult['native-country']=='India']
india['occupation'].value_counts()

