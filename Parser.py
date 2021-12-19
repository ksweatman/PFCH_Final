import csv
from math import nan
from re import U
from sys import dont_write_bytecode
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

colors = ['Navy','Blue','RoyalBlue','LightSkyBlue']
Yes_patch = mpatches.Patch(color='Navy', label="Yes")
No_patch = mpatches.Patch(color='Blue', label="No")
DR_patch = mpatches.Patch(color='RoyalBlue', label="Don't Remember")
DontUse_patch = mpatches.Patch(color='LightSkyBlue', label="Don't Use Library Website")


fig, ax = plt.subplots(figsize=(10,10))
_, _, autotexts = plt.pie(x,colors=colors, autopct='%1.1f%%',
    pctdistance=0.8,startangle=90,
    wedgeprops={'linewidth': 0.8, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},)
for autotext in autotexts:
    autotext.set_color('white')
ax.legend(handles=[Yes_patch,No_patch,DR_patch,DontUse_patch])             
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
#print(ListOther)

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

#Clarity
ClarityRatings=SurveyData['Clarity'].tolist
ClarityVeryPoor=0
ClarityPoor=0
ClarityAverage=0
ClarityGood=0
ClarityExcellent=0

for row in ClarityRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           ClarityVeryPoor=ClarityVeryPoor+1
       if 'Poor' in row:
           ClarityPoor=ClarityPoor+1
       if 'Average'in row:
           ClarityAverage=ClarityAverage+1
       if 'Good' in row:
           ClarityGood=ClarityGood+1
       if 'Excellent' in row:
           ClarityExcellent=ClarityExcellent+1

#convert to percentage
CTotal=(ClarityVeryPoor)+(ClarityPoor)+(ClarityAverage)+(ClarityGood)+(ClarityExcellent)
ClarityVeryPoorPerc=(ClarityVeryPoor/CTotal)*100
ClarityPoorPerc=(ClarityPoor/CTotal)*100
ClarityAveragePerc=(ClarityAverage/CTotal)*100
ClarityGoodPerc=(ClarityGood/CTotal)*100
ClarityExcellentPerc=(ClarityExcellent/CTotal)*100


#Navigation
NavRatings=SurveyData['Navigability'].tolist
NavVeryPoor=0
NavPoor=0
NavAverage=0
NavGood=0
NavExcellent=0
for row in NavRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           NavVeryPoor=NavVeryPoor+1
       if 'Poor' in row:
           NavPoor=NavPoor+1
       if 'Average'in row:
           NavAverage=NavAverage+1
       if 'Good' in row:
           NavGood=NavGood+1
       if 'Excellent' in row:
           NavExcellent=NavExcellent+1

#convert to percentage
NavTotal=(NavVeryPoor)+(NavPoor)+(NavAverage)+(NavGood)+(NavExcellent)
NavVeryPoorPerc=(NavVeryPoor/NavTotal)*100
NavPoorPerc=(NavPoor/NavTotal)*100
NavAveragePerc=(NavAverage/NavTotal)*100
NavGoodPerc=(NavGood/NavTotal)*100
NavExcellentPerc=(NavExcellent/NavTotal)*100

#Get Help

GHRatings=SurveyData['Getting Help'].tolist
GHVeryPoor=0
GHPoor=0
GHAverage=0
GHGood=0
GHExcellent=0
for row in GHRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           GHVeryPoor=GHVeryPoor+1
       if 'Poor' in row:
           GHPoor=GHPoor+1
       if 'Average'in row:
           GHAverage=GHAverage+1
       if 'Good' in row:
           GHGood=GHGood+1
       if 'Excellent' in row:
           GHExcellent=GHExcellent+1

#convert to percentage
GHTotal=(GHVeryPoor)+(GHPoor)+(GHAverage)+(GHGood)+(GHExcellent)
GHVeryPoorPerc=(GHVeryPoor/GHTotal)*100
GHPoorPerc=(GHPoor/GHTotal)*100
GHAveragePerc=(GHAverage/NavTotal)*100
GHGoodPerc=(GHGood/GHTotal)*100
GHExcellentPerc=(GHExcellent/GHTotal)*100

#Overall Rating

Ratings=SurveyData['Overall'].tolist
VeryPoor=0
Poor=0
Average=0
Good=0
Excellent=0
for row in Ratings():
    if type(row) != float:
       if 'Very Poor' in row:  
           VeryPoor=VeryPoor+1
       if 'Poor' in row:
           Poor=Poor+1
       if 'Average'in row:
           Average=Average+1
       if 'Good' in row:
           Good=Good+1
       if 'Excellent' in row:
           Excellent=Excellent+1

#convert to percentage
RatingTotal=(VeryPoor)+(Poor)+(Average)+(Good)+(Excellent)
RatingVeryPoorPerc=(VeryPoor/RatingTotal)*100
RatingPoorPerc=(Poor/RatingTotal)*100
RatingAveragePerc=(Average/RatingTotal)*100
RatingGoodPerc=(Good/RatingTotal)*100
RatingExcellentPerc=(Excellent/RatingTotal)*100

# Create DataFrame

data = [( VeryPoor,Poor,Average,Good,Excellent),
           (ClarityVeryPoor,ClarityPoor,ClarityAverage,ClarityGood,ClarityExcellent),
           (NavVeryPoor,NavPoor,NavAverage,NavGood,NavExcellent),
           (GHVeryPoor,GHPoor,GHAverage,GHGood,GHExcellent)]
  
ratingdata = pd.DataFrame(data, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
ratingdata.sort_index(inplace = True)
print(ratingdata)

#create percentage df

percent = [( RatingVeryPoorPerc,RatingPoorPerc,RatingAveragePerc,RatingGoodPerc,RatingExcellentPerc),
           (ClarityVeryPoorPerc,ClarityPoorPerc,ClarityAveragePerc,ClarityGoodPerc,ClarityExcellentPerc),
           (NavVeryPoorPerc,NavPoorPerc,NavAveragePerc,NavGoodPerc,NavExcellentPerc),
           (GHVeryPoorPerc,GHPoorPerc,GHAveragePerc,GHGoodPerc,GHExcellentPerc)]
  
ratingdataperc = pd.DataFrame(percent, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
ratingdataperc.sort_index(inplace = True)

#create stacked percentage bar chart

fig, ax = plt.subplots()

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Aspects')
plt.title('Library Website Ratings by Percentage')
plt.grid()
ratingdataperc.plot(kind='barh', color=['maroon','red','orange','yellow','green'], stacked=True,legend=False)
ax.set_xlim(xmin=0)
plt.xticks
plt.legend(bbox_to_anchor=(1.75, 1), loc='upper right', borderaxespad=0)
plt.savefig("webratings.png",bbox_inches='tight')