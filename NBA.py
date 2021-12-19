#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv("shots_data.csv")
df.head()


# In[25]:


a_c3_shots, a_c3_goals, a_nc3_shots, a_nc3_goals, a_2pt_shots, a_2pt_goals = 0,0,0,0,0,0
b_c3_shots, b_c3_goals, b_nc3_shots, b_nc3_goals, b_2pt_shots, b_2pt_goals = 0,0,0,0,0,0
for index,row in df.iterrows():
    team = row['team']
    x = row['x']
    y = row['y']
    goal = row['fgmade']
    hypo = np.sqrt(x*x + y*y)

    if team == 'Team A':
        if y<= 7.8 :
            if np.abs(x) >= 22 :
                a_c3_shots += 1
                if goal == 1:
                    a_c3_goals += 1
            else:
                a_2pt_shots += 1
                if goal == 1:
                    a_2pt_goals += 1
        else:
            if hypo >= 23.78 :
                a_nc3_shots += 1
                if goal == 1:
                    a_nc3_goals += 1
            else:
                a_2pt_shots += 1
                if goal == 1:
                    a_2pt_goals += 1
    elif team == 'Team B' :
        if y<= 7.8 :
            if np.abs(x) >= 22 :
                b_c3_shots += 1
                if goal == 1:
                    b_c3_goals += 1
            else:
                b_2pt_shots += 1
                if goal == 1:
                    b_2pt_goals += 1
        else:
            if hypo >= 23.78 :
                b_nc3_shots += 1
                if goal == 1:
                    b_nc3_goals += 1
            else:
                b_2pt_shots += 1
                if goal == 1:
                    b_2pt_goals += 1


# In[26]:


print(a_c3_shots, a_c3_goals, a_nc3_shots, a_nc3_goals, a_2pt_shots, a_2pt_goals)
print(b_c3_shots, b_c3_goals, b_nc3_shots, b_nc3_goals, b_2pt_shots, b_2pt_goals)


# In[33]:


a_total_shots = a_c3_shots + a_nc3_shots + a_2pt_shots
a_fgm = a_2pt_goals
a_3pm = a_c3_goals + a_nc3_goals
a_c3_percent = (a_c3_shots/a_total_shots)*100
a_nc3_percent = (a_nc3_shots/a_total_shots)*100
a_2pt_percent = (a_2pt_shots/a_total_shots)*100
a_efg_percent = (a_fgm + (0.5*a_3pm))/a_total_shots * 100
a_efg_percent_2pt = (a_fgm + (0.5*0))/a_total_shots * 100
a_efg_percent_3pt_corner = (0 + (0.5*a_c3_goals ))/a_total_shots * 100
a_efg_percent_3pt_non_corner = (0 + (0.5*a_nc3_goals ))/a_total_shots * 100
print("Team A shot distribution:")
print("C3 zone :", a_c3_percent)
print("NC3 zone :", a_nc3_percent)
print("2PT zone :", a_2pt_percent)
print("EFG % =", a_efg_percent)
print("EFG % =", a_efg_percent_2pt)
print("EFG % =",a_efg_percent_3pt_corner )
print("EFG % =",a_efg_percent_3pt_non_corner)
b_total_shots = b_c3_shots + b_nc3_shots + b_2pt_shots
b_fgm = b_2pt_goals
b_3pm = b_c3_goals + b_nc3_goals
b_c3_percent = (b_c3_shots/b_total_shots)*100
b_nc3_percent = (b_nc3_shots/b_total_shots)*100
b_2pt_percent = (b_2pt_shots/b_total_shots)*100
b_efg_percent = (b_fgm + (0.5*b_3pm))/b_total_shots * 100
b_efg_percent_2pt = (b_fgm + (0.5*0))/a_total_shots * 100
b_efg_percent_3pt_corner = (0 + (0.5*b_c3_goals))/a_total_shots * 100
b_efg_percent_3pt_non_corner = (0 + (0.5*b_nc3_goals))/a_total_shots * 100

print("\nTeam B shot distribution:")
print("C3 zone :", b_c3_percent)
print("NC3 zone :", b_nc3_percent)
print("2PT zone :", b_2pt_percent)
print("EFG % =", b_efg_percent)
print("EFG % =",b_efg_percent_2pt )
print("EFG % =",b_efg_percent_3pt_corner)
print("EFG % =",b_efg_percent_3pt_non_corner)


# In[ ]:
