import csv
from math import nan
from re import U
from sys import dont_write_bytecode
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

#Question: Did you find what you were looking for?

Visit=SurveyData.groupby("On your last visit to the library website, did you find what you were looking for? - Selected Choice")["On your last visit to the library website, did you find what you were looking for? - Selected Choice"].count()

Yes=Visit[3]
No=Visit[2]
DontRemember=Visit[0]
DontUse=Visit[1]

#create pie chart of respondent types

plt.style.use('_mpl-gallery-nogrid')

x = [Yes,No,DontRemember,DontUse]
labels=["Yes","No","Don't Remember","Don't Use Library Website"]

fig, ax = plt.subplots(figsize=(10,10))
ax.pie(x, labels=labels,autopct='%.1f%%', 
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)
          
ax.set_title('On your last visit to the library website, did you find what you were looking for?', fontsize=18, color='black')
plt.tight_layout()
plt.savefig("success.png")

#What other library websites do you use?-bar graph

LibList=SurveyData['What other library websites do you visit? - Selected Choice'].tolist()

NYPL=0
BPL=0
QPL=0
NYU=0
CooperUnion=0
Other=0
NA=0

for row in LibList:
    if type(row) != float:
       if 'New York Public Library' in row:  
           NYPL=NYPL+1
       if 'Brooklyn Public Library' in row:
           BPL=BPL+1
       if 'Queens Public Library'in row:
           QPL=QPL+1
       if 'NYU' in row:
           NYU=NYU+1
       if 'Cooper Union' in row:
           CooperUnion=CooperUnion+1
       if 'Other' in row:
           Other=Other+1
       if 'Not Applicable' in row:
           NA=NA+1

#create list of "Other" responses
ListOther=[]
for row in SurveyData['What other library websites do you visit? - Other - Text']:
    if type(row) != float:
        ListOther.append(row)
print(ListOther)

#bar plot
y=['New York Public Library','Brooklyn Public Library','Queens Public Library','NYU','Cooper Union','Other','None/Not Applicable']
x=[NYPL,BPL,QPL,NYU,CooperUnion,Other,NA]

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Library')
ax.set_ylabel('Responses')
plt.title('What other library websites do you visit?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax,)
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("libsites.png")

#Site Ratings-graph as stacked percentage bar chart

Clarity_Rating=SurveyData.groupby("Rate the following aspects of the website - Information Clarity")['Rate the following aspects of the website - Information Clarity'].count()
Clarity_Rating_Perc=(Clarity_Rating/len(SurveyData))*100
print(Clarity_Rating_Perc)
Nav_Rating=SurveyData.groupby("Rate the following aspects of the website - Navigability")['Rate the following aspects of the website - Navigability'].count()
Nav_Rating_Perc=(Nav_Rating/len(SurveyData))*100
print(Nav_Rating_Perc)
GetHelp_Rating=SurveyData.groupby("Rate the following aspects of the website - Getting Help")['Rate the following aspects of the website - Getting Help'].count()
GetHelp_Rating_Perc=(GetHelp_Rating/len(SurveyData))*100
print(GetHelp_Rating_Perc)
Rating=SurveyData.groupby("Rate the following aspects of the website - Overall Experience")['Rate the following aspects of the website - Overall Experience'].count()
Rating_Perc=(Rating/len(SurveyData))*100
print(Rating_Perc)

Categories=pd.Series(np.ndarray([]).tolist())
users=pd.Series(np.ndarray(int).tolist())

df=pd.concat([Categories,users],axis=1)

print(df)