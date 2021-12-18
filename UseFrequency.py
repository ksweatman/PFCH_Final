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

WebFreq=SurveyData['Web Use Frequency'].tolist()

WebUse=0

for row in WebFreq: 
   if type(row) != float:
       if  row not in WebUse:
           WebUse=WebUse+1

print(WebUse)

"""x=['To find out what technology is available for me to use', 'To find library hours', 'To reserve study space','To check on my loans','To get help from a library staff member','To find research materials','To find out about library locations','Other']
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
plt.savefig("webuses.png")"""

#Return results as stacked, grouped bar graph