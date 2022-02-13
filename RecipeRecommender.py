#!/usr/bin/env python
# coding: utf-8

# In[67]:


import requests
import json
import pandas as pd
import re


# In[68]:


df = pd.read_csv('dataframe.csv')
df.dropna(inplace=True)
df.drop(['Unnamed: 0','Image_Name','Ingredients'], axis=1, inplace=True)
df['Cleaned_Ingredients'] = df['Cleaned_Ingredients'].str.replace("\d+", '')
df['Cleaned_Ingredients'] = df['Cleaned_Ingredients'].str.replace("/", '')
df


# In[69]:


text_file = open("ingredients.txt", "r")
 
#read whole file to a string
ingre = text_file.read()

text_file.close()

ingredient_list = ingre.splitlines()
print(ingredient_list)

ingredient_dict = {}
for string in ingredient_list:
    if string not in ingredient_dict:
        ingredient_dict[string] = []

print(ingredient_dict)


# In[70]:


for ingredient in ingredient_list:
    ingredient_dict[ingredient] = df.loc[df['Cleaned_Ingredients'].str.contains(ingredient, case=False)]['Title'].values.tolist()
  


# In[71]:


ingredient_dict


# In[64]:


# append ingredient names to user_input_list
user_input_list = []
output = []

# create list of lists of recipes corresponding to each ingredient
for ingredient in user_input_list:
    output.append(ingredient_dict.get(ingredient))

# compare sets to find common recipes between all ingredients inputted
for i in range(1, len(output)):
    prev_lst = set(output[i-1])
    common_elements = prev_lst.intersection(output[i])

print(common_elements)


# In[65]:


# initialize dictionary of returned recipes as keys
recipes = dict.fromkeys(common_elements, 0)
print(recipes)


# In[66]:


# maps instructions as value to each recipe in dictionary
for r in recipes.keys():
    recipes[r] = df.loc[df['Title'].str.contains(r, case=False)]['Instructions'].values.tolist()
print(recipes)


# In[ ]:





# In[ ]:




