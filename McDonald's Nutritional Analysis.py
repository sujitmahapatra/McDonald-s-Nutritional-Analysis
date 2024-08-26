#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Read Dataset

# In[2]:


data = pd.read_csv('menu.csv')
data.head(5)


# In[3]:


data.shape


# # No. of Food Category

# In[10]:


plt.figure(figsize=(10, 4), dpi=100)
menu_category = data.Category.value_counts()
menu_category.plot.bar(color=['#FF5733', '#FFC300', '#DAF1A1', '#C70039', '#900C3F', '#581845', '#7D3C98', '#2E86C1', '#1ABC9C'])
plt.title("Number of Menu Items for each Food Category")
plt.ylabel("Count")
plt.xlabel("Menu Category")
plt.xticks(rotation=45)
plt.show()


# # Calories vs Calories from Fat

# In[6]:


plt.figure(figsize=(10, 4), dpi=100)

correlation = data['Calories'].corr(data['Calories from Fat'])
plt.scatter(data.Calories, data['Calories from Fat'], color='black')
plt.text(250, 1000, 'Correlation coefficient: {}'.format(round(correlation, 2)), fontsize=12)
plt.xlabel("Calories")
plt.ylabel("Calories from Fat")
plt.title("Relationship between Calories and Calories from Fat")
plt.show()


# # Mean of the 'Trans Fat'

# In[11]:


trans_fat_mean_by_category = data.groupby('Category')['Trans Fat'].mean()
print(trans_fat_mean_by_category)


# # % of Saturated Fat in Cholesterol

# In[12]:


data['saturated_cholesterol'] = (data['Saturated Fat'] / data['Cholesterol']) * 100


# # Top 5 Food Categories (Saturated Fat)

# In[13]:


saturated_cholesterol = data.groupby('Category')['saturated_cholesterol'].mean().dropna().nlargest(5)


# In[17]:


plt.figure(figsize=(10, 4), dpi=100)
saturated_cholesterol.sort_values(ascending=False).plot.bar(color = 'orange')
plt.title("Top 5 Food Categories: Saturated Fat Percentage in Cholesterol")
plt.ylabel("Percentage")
plt.xlabel("Menu Category")
plt.xticks(rotation=45)
plt.show();


# # Mean of all Categories

# In[18]:


coffee_tea = data[data.Category == 'Coffee & Tea']
coffee_tea.groupby('Item')['saturated_cholesterol'].mean().sort_values(ascending=False)


# In[19]:


shakes = data[data.Category == 'Smoothies & Shakes']
shakes.groupby('Item')['saturated_cholesterol'].mean().sort_values()


# In[20]:


beef_pork = data[data.Category == 'Beef & Pork']
beef_pork.groupby('Item')['saturated_cholesterol'].mean().sort_values()


# In[21]:


salads = data[data.Category == 'Salads']
salads.groupby('Item')['saturated_cholesterol'].mean().sort_values()


# In[22]:


chicken_fish = data[data.Category == 'Chicken & Fish']
chicken_fish.groupby('Item')['saturated_cholesterol'].mean().sort_values()


# In[23]:


data.groupby('Category')['Carbohydrates (% Daily Value)'].mean()


# # Total fat vs Total Carbohydrate

# In[24]:


plt.figure(figsize=(10, 4), dpi=100)
plt.scatter(data['Total Fat (% Daily Value)'], data['Carbohydrates (% Daily Value)'], color='k')
correlation = data['Total Fat (% Daily Value)'].corr(data['Carbohydrates (% Daily Value)'])
plt.text(125,20,'r = {}'.format(round(correlation,2)))
plt.xlabel("% Total Fat")
plt.ylabel("% Total Carbohydrate")
plt.title("Relationship between % Total Fat and % Total Carbohydrate")
plt.show()


# # Vitamins & Minerals

# In[25]:


data.groupby('Category')['Vitamin A (% Daily Value)'].mean()


# In[26]:


data.groupby('Category')['Vitamin C (% Daily Value)'].mean()


# In[27]:


beverage = data[data.Category == 'Beverages']
beverage.groupby('Item')['Vitamin C (% Daily Value)'].mean().sort_values()


# In[28]:


iron = data.groupby('Category')['Iron (% Daily Value)'].mean()
calcium = data.groupby('Category')['Calcium (% Daily Value)'].mean()


# In[33]:


plt.figure(figsize=(10, 4), dpi=100)

categories = iron.index
iron_values = iron.values
calcium_values = calcium.values

x_axis = np.arange(len(categories))

plt.bar(x_axis - 0.2, iron_values, 0.4, label='Iron', color='skyblue')
plt.bar(x_axis + 0.2, calcium_values, 0.4, label='Calcium', color='darkorange')

plt.xticks(x_axis, categories)
plt.xlabel("Menu Categories")
plt.title("Iron and Calcium Distribution in McDonald's Foods")
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[ ]:




