#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[2]:


df = pd.read_csv(r'C:\Users\tomin\Documents\Practicum Projects\Sprint 4\Car-Dashboard\vehicles_us.csv')
df.head()


# In[3]:


#filling in 0 for those without 4wd
df.is_4wd.fillna(0, inplace=True)


# In[4]:


#for the purpose of this project to view data in web application, dropping all rows with missing values
df = df.dropna()
df.head()


# In[5]:


#extracting the names of the manufacterer
split = df['model'].str.split(pat=' ', n=1, expand=True)
split


# In[6]:


#adding the manufacterer and model names into new columns, dropping the one with both 
df['manufacterer'] = split[0]
df['model_name'] = split[1]
df.drop('model', axis=1, inplace=True)
df.head()


# ## Plotly Dashboard

# In[7]:


#creating header 
st.header('Used Cars from, 1908-2019')
st.write("""
##### The data below shows the type of cars from each manufacterer from 1908-2019
""")
#inserting the dataframe
st.dataframe(df)
#let users decide whether they want to see the odometer or not using a checkbox
exclude_odometer = st.checkbox('Exclude odometer reading')


# In[8]:


exclude_odometer


# In[9]:


if exclude_odometer:
    df = df.drop('odometer', axis=1, inplace=True)


# In[10]:


st.header('Number of Vehicle Types by Manufacterer')
#creating a plotly histogram
fig1 = px.histogram(df, x='manufacterer', color='type')
#displaying the figure with streamlit
st.write(fig1)


# In[11]:


fig1.show()


# In[12]:


st.header('Price Range of Vehicles Per Model Year')
#creating a scatterplot
fig2 = px.scatter(df, x='model_year', y='price')
#displaying the scatterplot
st.write(fig2)


# In[13]:


fig2.show()


# In[14]:


st.header('Overall Transmission Type of Vehicles')
st.write("""
##### The data below that the majority of cars listed are automatic transmission.
""")
#making a histogram
fig3 = px.histogram(df, x='transmission')
#displaying the histogram
st.write(fig3)


# In[15]:


fig3.show()


# In[16]:


#filtering the most popular types of vehicles in the US
us_cars = df[(df['type'] == 'SUV') | (df['type'] == 'sedan') | (df['type'] == 'truck') | (df['type'] == 'mini-van')]
us_cars


# In[17]:


st.header('Overall Types of Cars Listed')
#creating a scatterplot
fig4 = px.histogram(us_cars, x='type')
#displaying the scatterplot
st.write(fig4)


# In[18]:


fig4.show()


# In[19]:


st.header('Price of Cars')
#creating a scatterplot
fig5 = px.scatter(us_cars, x='model_year', y='price')
#displaying the scatterplot
st.write(fig5)


# In[20]:


fig5.show()

