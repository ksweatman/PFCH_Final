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


"""y=['Available Technology', 'Library Hours', 'Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
x=[Use1,Use2,Use3,Use4,Use5,Use6,Use7,Use8]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Why do you use the library website?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax,orient='h')
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("webuses.png")"""

#Faculty Dataset
FacUse=FacData['Web Uses'].tolist()

FacUse1=0
FacUse2=0
FacUse3=0
FacUse4=0
FacUse5=0
FacUse6=0
FacUse7=0
FacUse8=0
for row in Use: 
   if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           FacUse1=FacUse1+1
       if 'To find library hours' in row:
           FacUse2=FacUse2+1
       if'To reserve study space'in row:
           FacUse3=FacUse3+1
       if 'To check on my loans' in row:
           FacUse4=FacUse4+1
       if 'To get help from a library staff member' in row:
           FacUse5=FacUse5+1
       if 'To find research materials' in row:
           FacUse6=FacUse6+1
       if 'To find out about library locations' in row:
           FacUse7=FacUse7+1
       if 'Other' in row:
           FacUse8=FacUse8+1


"""y=['Available Technology', 'Library Hours', 'Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
x=[FacUse1,FacUse2,FacUse3,FacUse4,FacUse5,FacUse6,FacUse7,FacUse8]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Faculty Responses: Why do you use the library website?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax,orient='h',color="Blue")
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("webfacuses.png")"""

#Student Dataset

StudentUse=StudentData['Web Uses'].tolist()

StudentUse1=0
StudentUse2=0
StudentUse3=0
StudentUse4=0
StudentUse5=0
StudentUse6=0
StudentUse7=0
StudentUse8=0
for row in StudentUse: 
   if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           StudentUse1=StudentUse1+1
       if 'To find library hours' in row:
           StudentUse2=StudentUse2+1
       if'To reserve study space'in row:
           StudentUse3=StudentUse3+1
       if 'To check on my loans' in row:
           StudentUse4=StudentUse4+1
       if 'To get help from a library staff member' in row:
           StudentUse5=StudentUse5+1
       if 'To find research materials' in row:
           StudentUse6=StudentUse6+1
       if 'To find out about library locations' in row:
           StudentUse7=StudentUse7+1
       if 'Other' in row:
           StudentUse8=StudentUse8+1

"""Uses=['Available Technology','Library Hours','Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
Responses=[StudentUse1,StudentUse2,StudentUse3,StudentUse4,StudentUse5,StudentUse6,StudentUse7,StudentUse8]
fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Student Responses: Why do you use the library website?')
plt.grid()
bar_plot = sns.barplot(x=Responses, y=Uses, ax=ax,orient='h',color="Red")
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("webstudentuses.png")"""

# Create DataFrame
data = {'Uses':['Available Technology','Available Technology','Library Hours','Library Hours','Reserve Study Space','Reserve Study Space','Check my Loans','Check my Loans','Get Help from Library Staff','Get Help from Library Staff','Find Research Materials','Find Research Materials','Library Locations','Library Locations','Other','Other'],
        'Respondent':['Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students'],
        'Responses':[FacUse1,StudentUse1,FacUse2,StudentUse2,FacUse3,StudentUse3,FacUse4,StudentUse4,FacUse5,StudentUse5,FacUse6,StudentUse6,FacUse7,StudentUse7,FacUse8,StudentUse8]
}

df = pd.DataFrame(data)
df.pivot("Uses", "Respondent","Responses")

#Grouped Bar Plot
colors = ["blue", "red"]
sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(10,10))
plt.grid()
bar_plot = sns.barplot(
    x="Uses", 
    y="Responses", 
    hue="Respondent", 
    data=df, 
    ci=None
    )
ax.set_title('Why do you use the library website?')
ax.set_ylabel('Responses')
ax.set_xlabel('Uses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("webusegroup.png")