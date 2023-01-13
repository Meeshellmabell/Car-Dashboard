#!/usr/bin/env python
# coding: utf-8

# # Car Dashboard
# This notebook contains data of used cars from 1908-2019. We fill clean the data and make some histograms and a scatterplot to deploy an app on Render. 

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[2]:


df = pd.read_csv(r'C:\Users\tomin\Documents\Practicum Projects\Sprint 4\Car-Dashboard\vehicles_us.csv')
df.head()


# In[3]:


df.info()


# There are some columns with missing values such as model_year, cylinders, odometer, paint_color, and is_4wd. 

# In[4]:


#filling in missing values in model_year with median based on car model 
df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'))


# In[5]:


#filling in 0 for those without 4wd
df.is_4wd.fillna(0, inplace=True)


# In[6]:


#filling in missing values in cylinders based on car model 
df['cylinders'] = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('median'))


# In[7]:


#filing in missing values in odometer based on model and model_year
df['odometer'] = df['odometer'].fillna(df.groupby(['model','model_year'])['odometer'].transform('median'))


# In[8]:


#filling in the missing values with unknown for paint_color 
df.paint_color.fillna('unknown', inplace=True)


# In[9]:


#looking to make sure there are no missing values before proceeding 
df.info()


# In[10]:


#extracting the names of the manufacterer
split = df['model'].str.split(pat=' ', n=1, expand=True)


# In[11]:


#adding the manufacterer and model names into new columns, dropping the one with both 
df['manufacterer'] = split[0]
df['model_name'] = split[1]
df.drop('model', axis=1, inplace=True)
df.head()


# ## Plotly Dashboard

# In[12]:


#creating header 
st.header('Used Cars from, 1908-2019')
st.write("""
##### The data below shows the type of cars from each manufacterer from 1908-2019
""")
#let users decide whether they want to see the odometer or not using a checkbox
exclude_odometer = st.checkbox('Exclude odometer reading')
if exclude_odometer:
    df = df.drop('odometer', axis=1)
#inserting the dataframe
st.dataframe(df)


# In[13]:


st.header('Number of Vehicle Types by Manufacterer')
#creating a plotly histogram
fig1 = px.histogram(df, x='manufacterer', color='type')
#displaying the figure with streamlit
st.write(fig1)


# In[14]:


st.header('Price Range of Vehicles Per Model Year')
#creating a scatterplot
fig2 = px.scatter(df, x='model_year', y='price')
#displaying the scatterplot
st.write(fig2)


# In[15]:


st.header('Overall Transmission Type of Vehicles')
st.write("""
##### The data below that the majority of cars listed are automatic transmission.
""")
#making a histogram
fig3 = px.histogram(df, x='transmission')
#displaying the histogram
st.write(fig3)


# In[16]:


st.header('Overall Types of Cars Listed')
#creating a scatterplot
fig4 = px.histogram(df, x='type')
#displaying the scatterplot
st.write(fig4)


# ### Conclusion:
# We have managed to clean the data and take a look at the number of vehicles per manufacterer, the overall price range for all the vehicles listed, the transmission type of the vehicles, and types of vehicles listed in this data. 

# In[ ]:




