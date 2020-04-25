#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Rustem_Yeleussinov/OneDrive - EPAM/04_Training and Education/10_Certification/Udacity/DA/weather.csv')
df.head()


# In[2]:


df_pivot = pd.pivot_table(df, values = ['local_avg_temp','global_avg_temp'],index = 'year')
df_pivot.head()


# In[4]:


df_pivot['moving_avg_10_local'] = df_pivot.iloc[:,0].rolling(window=10).mean()
df_pivot.head(15)


# In[5]:


trace0 = go.Scatter(
    x = df_pivot.index,
    y = df_pivot.moving_avg_10_global,
    mode = 'lines',
    name = 'Global Avg Temp'
)

trace1 = go.Scatter(
    x = df_pivot.index,
    y = df_pivot.moving_avg_10_local,
    mode = 'lines',
    name = 'San Jose Avg Temp'    
)


# In[6]:


data = [trace0, trace1]


# In[7]:


layout = go.Layout(title = '10 years moving average Global vs San Jose', xaxis_title="Years",
    yaxis_title="Temperature",)


# In[8]:


figure = go.Figure(data = data, layout = layout)
pyo.plot(figure)

