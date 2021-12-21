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

#return responses to first 2 survey questions

#Overall Responses

LibFreqs=SurveyData['Library Use Frequency'].tolist()
WebFreqs=SurveyData['Web Use Frequency'].tolist()

WebFreq1=0
WebFreq2=0
WebFreq3=0
WebFreq4=0
WebFreq5=0
WebFreq6=0
WebFreq7=0

for row in WebFreqs:
    if type(row) != float:
       if 'Multiple visits for day' in row:  
           WebFreq1=WebFreq1+1
       if 'Once a day' in row:
           WebFreq2=WebFreq2+1
       if'2-3 times per week'in row:
           WebFreq3=WebFreq3+1
       if 'Once a week' in row:
           WebFreq4=WebFreq4+1
       if '2-3 times per month' in row:
           WebFreq5=WebFreq5+1
       if 'Once per semester' in row:
           WebFreq6=WebFreq6+1
       if 'Never' in row:
           WebFreq7=WebFreq7+1


LibFreq1=0
LibFreq2=0
LibFreq3=0
LibFreq4=0
LibFreq5=0
LibFreq6=0
LibFreq7=0

for row in LibFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           LibFreq1=LibFreq1+1
       if 'Once a day' in row:
           LibFreq2=LibFreq2+1
       if'2-3 times per week'in row:
           LibFreq3=LibFreq3+1
       if 'Once a week' in row:
           LibFreq4=LibFreq4+1
       if '2-3 times per month' in row:
           LibFreq5=LibFreq5+1
       if 'Once per semester' in row:
           LibFreq6=LibFreq6+1
       if 'Never' in row:
           LibFreq7=LibFreq7+1

#bar plot-library vs. web use frequency

#Student Responses

StudentLibFreqs=StudentData['Library Use Frequency'].tolist()
StudentWebFreqs=StudentData['Web Use Frequency'].tolist()

StudentWebFreq1=0
StudentWebFreq2=0
StudentWebFreq3=0
StudentWebFreq4=0
StudentWebFreq5=0
StudentWebFreq6=0
StudentWebFreq7=0

for row in StudentWebFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           StudentWebFreq1=StudentWebFreq1+1
       if 'Once a day' in row:
           StudentWebFreq2=StudentWebFreq2+1
       if'2-3 times per week'in row:
           StudentWebFreq3=StudentWebFreq3+1
       if 'Once a week' in row:
           StudentWebFreq4=StudentWebFreq4+1
       if '2-3 times per month' in row:
           StudentWebFreq5=StudentWebFreq5+1
       if 'Once per semester' in row:
           StudentWebFreq6=StudentWebFreq6+1
       if 'Never' in row:
           StudentWebFreq7=StudentWebFreq7+1


StudentLibFreq1=0
StudentLibFreq2=0
StudentLibFreq3=0
StudentLibFreq4=0
StudentLibFreq5=0
StudentLibFreq6=0
StudentLibFreq7=0

for row in StudentLibFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           StudentLibFreq1=StudentLibFreq1+1
       if 'Once a day' in row:
           StudentLibFreq2=StudentLibFreq2+1
       if'2-3 times per week'in row:
           StudentLibFreq3=StudentLibFreq3+1
       if 'Once a week' in row:
           StudentLibFreq4=StudentLibFreq4+1
       if '2-3 times per month' in row:
           StudentLibFreq5=StudentLibFreq5+1
       if 'Once per semester' in row:
           StudentLibFreq6=StudentLibFreq6+1
       if 'Never' in row:
           StudentLibFreq7=StudentLibFreq7+1


# Create DataFrame
data = {'Use Frequency':['Multiple visits per day','Multiple visits per day','Once a day','Once a day','2-3 times per week','2-3 times per week','Once a week','Once a week','2-3 times per month','2-3 times per month','Once per semester','Once per semester','Never','Never'],
        'Use Type':['Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person'],
        'Responses':[StudentWebFreq1,StudentLibFreq1,StudentWebFreq2,StudentLibFreq2,StudentWebFreq3,StudentLibFreq3,StudentWebFreq4,StudentLibFreq4,StudentWebFreq5,StudentLibFreq5,StudentWebFreq6,StudentLibFreq6,StudentWebFreq7,StudentLibFreq7]
}

df = pd.DataFrame(data)
df.pivot("Use Frequency", "Use Type","Responses")

#Grouped Bar Plot
fig, ax = plt.subplots(figsize=(10,10))
plt.grid()
colors = ['#F50000','#FF7070']
sns.set_palette(sns.color_palette(colors))
bar_plot = sns.barplot(
    x="Use Frequency", 
    y="Responses", 
    hue="Use Type", 
    data=df, 
    ci=None
    )
ax.set_title('Student Responses: How Often do you Use Library Resources?')
ax.set_ylabel('Responses')
ax.set_xlabel('Use Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/studentusefreq.png")

#Faculty Responses

FacLibFreqs=FacData['Library Use Frequency'].tolist()
FacWebFreqs=FacData['Web Use Frequency'].tolist()

FacWebFreq1=0
FacWebFreq2=0
FacWebFreq3=0
FacWebFreq4=0
FacWebFreq5=0
FacWebFreq6=0
FacWebFreq7=0

for row in FacWebFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           FacWebFreq1=FacWebFreq1+1
       if 'Once a day' in row:
           FacWebFreq2=FacWebFreq2+1
       if'2-3 times per week'in row:
           FacWebFreq3=FacWebFreq3+1
       if 'Once a week' in row:
           FacWebFreq4=FacWebFreq4+1
       if '2-3 times per month' in row:
           FacWebFreq5=FacWebFreq5+1
       if 'Once per semester' in row:
           FacWebFreq6=FacWebFreq6+1
       if 'Never' in row:
           FacWebFreq7=FacWebFreq7+1

FacLibFreq1=0
FacLibFreq2=0
FacLibFreq3=0
FacLibFreq4=0
FacLibFreq5=0
FacLibFreq6=0
FacLibFreq7=0

for row in FacLibFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           FacLibFreq1=FacLibFreq1+1
       if 'Once a day' in row:
           FacLibFreq2=FacLibFreq2+1
       if '2-3 times per week'in row:
           FacLibFreq3=FacLibFreq3+1
       if 'Once a week' in row:
           FacLibFreq4=FacLibFreq4+1
       if '2-3 times per month' in row:
           FacLibFreq5=FacLibFreq5+1
       if 'Once per semester' in row:
           FacLibFreq6=FacLibFreq6+1
       if 'Never' in row:
           FacLibFreq7=FacLibFreq7+1

# Create DataFrame
data = {'Use Frequency':['Multiple visits per day','Multiple visits per day','Once a day','Once a day','2-3 times per week','2-3 times per week','Once a week','Once a week','2-3 times per month','2-3 times per month','Once per semester','Once per semester','Never','Never'],
        'Use Type':['Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person'],
        'Responses':[FacWebFreq1,FacLibFreq1,FacWebFreq2,FacLibFreq2,FacWebFreq3,FacLibFreq3,FacWebFreq4,FacLibFreq4,FacWebFreq5,FacLibFreq5,FacWebFreq6,FacLibFreq6,FacWebFreq7,FacLibFreq7]
}

df = pd.DataFrame(data)
df.pivot("Use Frequency", "Use Type","Responses")

#Grouped Bar Plot
fig, ax = plt.subplots(figsize=(10,10))
colors = ['#04578B','#40AEF2']
sns.set_palette(sns.color_palette(colors))
plt.grid()
bar_plot = sns.barplot(
    x="Use Frequency", 
    y="Responses", 
    hue="Use Type", 
    data=df, 
    ci=None
    )
ax.set_title('Faculty Responses: How Often do you Use Library Resources?')
ax.set_ylabel('Responses')
ax.set_xlabel('Use Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/facusefreq.png")

#Overall plot
# Create DataFrame
data = {'Use Frequency':['Multiple visits per day','Multiple visits per day','Multiple visits per day','Multiple visits per day','Once a day','Once a day','Once a day','Once a day','2-3 times per week','2-3 times per week','2-3 times per week','2-3 times per week','Once a week','Once a week','Once a week','Once a week','2-3 times per month','2-3 times per month','2-3 times per month','2-3 times per month','Once per semester','Once per semester','Once per semester','Once per semester','Never','Never','Never','Never'],
        'Use Type':['Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person'],
        'Respondent':['Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student'],
        'Responses':[FacWebFreq1,FacLibFreq1,StudentWebFreq1,StudentLibFreq1,FacWebFreq2,FacLibFreq2,StudentWebFreq2,StudentLibFreq2,FacWebFreq3,FacLibFreq3,StudentWebFreq3,StudentLibFreq3,FacWebFreq4,FacLibFreq4,StudentWebFreq4,StudentLibFreq4,FacWebFreq5,FacLibFreq5,StudentWebFreq5,StudentLibFreq5,FacWebFreq6,FacLibFreq6,StudentWebFreq6,StudentLibFreq6,FacWebFreq7,FacLibFreq7,StudentWebFreq7,StudentLibFreq7]
}

df = pd.DataFrame(data)
colors = ['#3F6E35','#8FC383']
sns.set_palette(sns.color_palette(colors))
df.pivot(index=['Respondent','Use Type'], columns=['Use Frequency'], values=['Responses'])
sns.catplot(x="Respondent", y="Responses",
                 hue="Use Type", col="Use Frequency",
                 data=df, kind="bar",
                 height=4, aspect=.7)
ax.set_title('Library Resource Use Frequency')
#plt.tight_layout()
plt.savefig("Charts/usefreq.png")

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


y=['Available Technology', 'Library Hours', 'Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
x=[Use1,Use2,Use3,Use4,Use5,Use6,Use7,Use8]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Why do you use the library website?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax,orient='h',color='green')
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("Charts/webuses.png")

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


y=['Available Technology', 'Library Hours', 'Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
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
plt.savefig("Charts/webfacuses.png")

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

Uses=['Available Technology','Library Hours','Reserve Study Space','Check my Loans','Get Help from Library Staff','Find Research Materials','Library Locations','Other']
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
plt.savefig("Charts/webstudentuses.png")

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
plt.savefig("Charts/webusegroup.png")

#In-Person Library Uses
LibUse=SurveyData['Library Uses'].tolist()

LibUse1=0
LibUse2=0
LibUse3=0
LibUse4=0
LibUse5=0
LibUse6=0
LibUse7=0
for row in LibUse: 
   if type(row) != float:
       if 'To print or scan documents' in row:  
           LibUse1=LibUse1+1
       if 'To use the public desktops or circulating laptops' in row:
           LibUse2=LibUse2+1
       if 'To use a private/bookable space'in row:
           LibUse3=LibUse3+1
       if 'To use a public study area' in row:
           LibUse4=LibUse4+1
       if 'To get research help from a library staff member' in row:
           LibUse5=LibUse5+1
       if 'To browse the stacks/find resources' in row:
           LibUse6=LibUse6+1
       if 'Other' in row:
           LibUse7=LibUse7+1

LibUses=['Printing and Scanning', 'Use Public or Circulating Computers', 'Private Study Space','Public Study Area','Get Help from Library Staff','Browse/Find Research Materials','Other']
LibUseResponses=[LibUse1,LibUse2,LibUse3,LibUse4,LibUse5,LibUse6,LibUse7]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Why do come to the library in person?')
plt.grid()
bar_plot = sns.barplot(LibUseResponses, LibUses, ax=ax,orient='h',color='green')
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("Charts/libuses.png")

#Faculty Dataset
FacLibUse=FacData['Library Uses'].tolist()

FacLibUse1=0
FacLibUse2=0
FacLibUse3=0
FacLibUse4=0
FacLibUse5=0
FacLibUse6=0
FacLibUse7=0
FacLibUse8=0
for row in FacLibUse: 
   if type(row) != float:
       if 'To print or scan documents' in row:  
           FacLibUse1=FacLibUse1+1
       if 'To use the public desktops or circulating laptops' in row:
           FacLibUse2=FacLibUse2+1
       if 'To use a private/bookable space'in row:
           FacLibUse3=FacLibUse3+1
       if 'To use a public study area' in row:
           FacLibUse4=FacLibUse4+1
       if 'To get research help from a library staff member' in row:
           FacLibUse5=FacLibUse5+1
       if 'To browse the stacks/find resources' in row:
           FacLibUse6=FacLibUse6+1
       if 'Other' in row:
           FacLibUse7=FacLibUse7+1


FacLibUses=['Printing and Scanning', 'Use Public or Circulating Computers', 'Private Study Space','Public Study Area','Get Help from Library Staff','Browse/Find Research Materials','Other']
FacLibUseResponses=[FacLibUse1,FacLibUse2,FacLibUse3,FacLibUse4,FacLibUse5,FacLibUse6,FacLibUse7]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Faculty Responses: Why do come to the library in person?')
plt.grid()
bar_plot = sns.barplot(FacLibUseResponses, FacLibUses, ax=ax,orient='h',color="blue")
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("Charts/faclibuses.png")

#Student Dataset

StudentLibUse=StudentData['Library Uses'].tolist()

StudentLibUse1=0
StudentLibUse2=0
StudentLibUse3=0
StudentLibUse4=0
StudentLibUse5=0
StudentLibUse6=0
StudentLibUse7=0
StudentLibUse8=0
for row in StudentLibUse: 
   if type(row) != float:
       if 'To print or scan documents' in row:  
           StudentLibUse1=StudentLibUse1+1
       if 'To use the public desktops or circulating laptops' in row:
           StudentLibUse2=StudentLibUse2+1
       if 'To use a private/bookable space'in row:
           StudentLibUse3=StudentLibUse3+1
       if 'To use a public study area' in row:
           StudentLibUse4=StudentLibUse4+1
       if 'To get research help from a library staff member' in row:
           StudentLibUse5=StudentLibUse5+1
       if 'To browse the stacks/find resources' in row:
           StudentLibUse6=StudentLibUse6+1
       if 'Other' in row:
           StudentLibUse7=StudentLibUse7+1

StudentLibUses=['Printing and Scanning', 'Use Public or Circulating Computers', 'Private Study Space','Public Study Area','Get Help from Library Staff','Browse/Find Research Materials','Other']
StudentLibUseResponses=[StudentLibUse1,StudentLibUse2,StudentLibUse3,StudentLibUse4,StudentLibUse5,StudentLibUse6,StudentLibUse7]
fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Uses')
plt.title('Student Responses: Why do come to the library in person?')
plt.grid()
bar_plot = sns.barplot(x=StudentLibUseResponses, y=StudentLibUses, ax=ax,orient='h',color="Red")
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("Charts/studentlibuses.png")

# Create DataFrame
data = {'LibUses':['Printing and Scanning', 'Printing and Scanning','Use Public or Circulating Computers','Use Public or Circulating Computers', 'Private Study Space','Private Study Space','Public Study Area','Public Study Area','Get Help from Library Staff','Get Help from Library Staff','Browse/Find Research Materials','Browse/Find Research Materials','Other','Other'],
        'Respondent':['Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students','Faculty','Students'],
        'LibUseResponses':[FacLibUse1,StudentLibUse1,FacLibUse2,StudentLibUse2,FacLibUse3,StudentLibUse3,FacLibUse4,StudentLibUse4,FacLibUse5,StudentLibUse5,FacLibUse6,StudentLibUse6,FacLibUse7,StudentLibUse7]
}

df = pd.DataFrame(data)
df.pivot("LibUses", "Respondent","LibUseResponses")
#Grouped Bar Plot
colors = ["blue", "red"]
sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(10,10))
plt.grid()
bar_plot = sns.barplot(
    x="LibUses", 
    y="LibUseResponses", 
    hue="Respondent", 
    data=df, 
    ci=None
    )
ax.set_title('Why do come to the library in person?')
ax.set_ylabel('Responses')
ax.set_xlabel('Uses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/libusegroup.png")
