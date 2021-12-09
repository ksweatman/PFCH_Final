import csv
from math import nan
from re import U
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import collections, operator
import seaborn as sns


#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

Use=SurveyData['Web Uses'].tolist()

Use1=0
Use2=0
Use3=0
Use4=0
Use5=0
Use6=0
Use7=0
Use8=0
for row in Use: 
   if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           Use1=Use1+1
       if 'To find library hours' in row:
           Use2=Use2+1
       if'To reserve study space'in row:
           Use3=Use3+1
       if 'To check on my loans' in row:
           Use4=Use4+1
       if 'To get help from a library staff member' in row:
           Use5=Use5+1
       if 'To find research materials' in row:
           Use6=Use6+1
       if 'To find out about library locations' in row:
           Use7=Use7+1
       if 'Other' in row:
           Use8=Use8+1


x=['To find out what technology is available for me to use', 'To find library hours', 'To reserve study space','To check on my loans','To get help from a library staff member','To find research materials','To find out about library locations','Other']
y=[Use1,Use2,Use3,Use4,Use5,Use6,Use7,Use8]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Respondents')
ax.set_xlabel('Uses')
plt.title('Why do you use the library website?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax)
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("webuses.png")
