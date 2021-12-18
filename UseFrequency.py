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
plt.savefig("studentusefreq.png")

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
plt.savefig("facusefreq.png")

#Overall plot
# Create DataFrame
data = {'Use Frequency':['Multiple visits per day','Multiple visits per day','Multiple visits per day','Multiple visits per day','Once a day','Once a day','Once a day','Once a day','2-3 times per week','2-3 times per week','2-3 times per week','2-3 times per week','Once a week','Once a week','Once a week','Once a week','2-3 times per month','2-3 times per month','2-3 times per month','2-3 times per month','Once per semester','Once per semester','Once per semester','Once per semester','Never','Never','Never','Never'],
        'Use Type':['Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person','Online','In Person'],
        'Respondent':['Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student','Faculty','Faculty','Student','Student'],
        'Responses':[FacWebFreq1,FacLibFreq1,StudentWebFreq1,StudentLibFreq1,FacWebFreq2,FacLibFreq2,StudentWebFreq2,StudentLibFreq2,FacWebFreq3,FacLibFreq3,StudentWebFreq3,StudentLibFreq3,FacWebFreq4,FacLibFreq4,StudentWebFreq4,StudentLibFreq4,FacWebFreq5,FacLibFreq5,StudentWebFreq5,StudentLibFreq5,FacWebFreq6,FacLibFreq6,StudentWebFreq6,StudentLibFreq6,FacWebFreq7,FacLibFreq7,StudentWebFreq7,StudentLibFreq7]
}

df = pd.DataFrame(data)
df.pivot(index=['Respondent','Use Type'], columns=['Use Frequency'], values=['Responses'])
sns.catplot(x="Respondent", y="Responses",
                 hue="Use Type", col="Use Frequency",
                 data=df, kind="bar",
                 height=4, aspect=.7)
ax.set_title('Library Resource Use Frequency')
#plt.tight_layout()
plt.savefig("usefreq.png")
