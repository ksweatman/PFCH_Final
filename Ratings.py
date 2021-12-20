import csv
from math import nan
from re import U
from sys import dont_write_bytecode
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import numpy as np
import collections, operator
import seaborn as sns

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

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
ratingdataperc.plot(kind='barh', color=['#182914','#284521','#3F6E35','#5FA550','#8FC383'], stacked=True,legend=False).set(title="Library Website Ratings by Percentage")
ax.set_xlim(xmin=0)
plt.xticks
plt.legend(bbox_to_anchor=(1.75, 1), loc='upper right', borderaxespad=0)
plt.savefig("Charts/webratings.png",bbox_inches='tight')

#Faculty Ratings

#Clarity
FacClarityRatings=FacData['Clarity'].tolist
FacClarityVeryPoor=0
FacClarityPoor=0
FacClarityAverage=0
FacClarityGood=0
FacClarityExcellent=0

for row in FacClarityRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           FacClarityVeryPoor=FacClarityVeryPoor+1
       if 'Poor' in row:
           FacClarityPoor=FacClarityPoor+1
       if 'Average'in row:
           FacClarityAverage=FacClarityAverage+1
       if 'Good' in row:
           FacClarityGood=FacClarityGood+1
       if 'Excellent' in row:
           FacClarityExcellent=FacClarityExcellent+1

#convert to percentage
FacCTotal=(FacClarityVeryPoor)+(FacClarityPoor)+(FacClarityAverage)+(FacClarityGood)+(FacClarityExcellent)
FacClarityVeryPoorPerc=(FacClarityVeryPoor/FacCTotal)*100
FacClarityPoorPerc=(FacClarityPoor/FacCTotal)*100
FacClarityAveragePerc=(FacClarityAverage/FacCTotal)*100
FacClarityGoodPerc=(FacClarityGood/FacCTotal)*100
FacClarityExcellentPerc=(FacClarityExcellent/FacCTotal)*100


#Navigation
FacNavRatings=FacData['Navigability'].tolist
FacNavVeryPoor=0
FacNavPoor=0
FacNavAverage=0
FacNavGood=0
FacNavExcellent=0
for row in FacNavRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           FacNavVeryPoor=FacNavVeryPoor+1
       if 'Poor' in row:
           FacNavPoor=FacNavPoor+1
       if 'Average'in row:
           FacNavAverage=FacNavAverage+1
       if 'Good' in row:
           FacNavGood=FacNavGood+1
       if 'Excellent' in row:
           FacNavExcellent=FacNavExcellent+1

#convert to percentage
FacNavTotal=(FacNavVeryPoor)+(FacNavPoor)+(FacNavAverage)+(FacNavGood)+(FacNavExcellent)
FacNavVeryPoorPerc=(FacNavVeryPoor/FacNavTotal)*100
FacNavPoorPerc=(FacNavPoor/FacNavTotal)*100
FacNavAveragePerc=(FacNavAverage/FacNavTotal)*100
FacNavGoodPerc=(FacNavGood/FacNavTotal)*100
FacNavExcellentPerc=(FacNavExcellent/FacNavTotal)*100

#Get Help

FacGHRatings=FacData['Getting Help'].tolist
FacGHVeryPoor=0
FacGHPoor=0
FacGHAverage=0
FacGHGood=0
FacGHExcellent=0
for row in FacGHRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           FacGHVeryPoor=FacGHVeryPoor+1
       if 'Poor' in row:
           FacGHPoor=FacGHPoor+1
       if 'Average'in row:
           FacGHAverage=FacGHAverage+1
       if 'Good' in row:
           FacGHGood=FacGHGood+1
       if 'Excellent' in row:
           FacGHExcellent=FacGHExcellent+1

#convert to percentage
FacGHTotal=(FacGHVeryPoor)+(FacGHPoor)+(FacGHAverage)+(FacGHGood)+(FacGHExcellent)
FacGHVeryPoorPerc=(FacGHVeryPoor/FacGHTotal)*100
FacGHPoorPerc=(FacGHPoor/FacGHTotal)*100
FacGHAveragePerc=(FacGHAverage/FacGHTotal)*100
FacGHGoodPerc=(FacGHGood/FacGHTotal)*100
FacGHExcellentPerc=(FacGHExcellent/FacGHTotal)*100

#Overall Rating

FacRatings=FacData['Overall'].tolist
FacVeryPoor=0
FacPoor=0
FacAverage=0
FacGood=0
FacExcellent=0
for row in FacRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           FacVeryPoor=FacVeryPoor+1
       if 'Poor' in row:
           FacPoor=FacPoor+1
       if 'Average'in row:
           FacAverage=FacAverage+1
       if 'Good' in row:
           FacGood=FacGood+1
       if 'Excellent' in row:
           FacExcellent=FacExcellent+1

#convert to percentage
FacRatingTotal=(FacVeryPoor)+(FacPoor)+(FacAverage)+(FacGood)+(FacExcellent)
FacRatingVeryPoorPerc=(FacVeryPoor/FacRatingTotal)*100
FacRatingPoorPerc=(FacPoor/FacRatingTotal)*100
FacRatingAveragePerc=(FacAverage/FacRatingTotal)*100
FacRatingGoodPerc=(FacGood/FacRatingTotal)*100
FacRatingExcellentPerc=(FacExcellent/FacRatingTotal)*100

# Create DataFrame

FacRatingdata = [( FacVeryPoor,FacPoor,FacAverage,FacGood,FacExcellent),
           (FacClarityVeryPoor,FacClarityPoor,FacClarityAverage,FacClarityGood,FacClarityExcellent),
           (FacNavVeryPoor,FacNavPoor,FacNavAverage,FacNavGood,FacNavExcellent),
           (FacGHVeryPoor,FacGHPoor,FacGHAverage,FacGHGood,FacGHExcellent)]
  
Fac_stackratingdata = pd.DataFrame(FacRatingdata, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
Fac_stackratingdata.sort_index(inplace = True)
print(Fac_stackratingdata)

#create percentage df

Facpercent = [( FacRatingVeryPoorPerc,FacRatingPoorPerc,FacRatingAveragePerc,FacRatingGoodPerc,FacRatingExcellentPerc),
           (FacClarityVeryPoorPerc,FacClarityPoorPerc,FacClarityAveragePerc,FacClarityGoodPerc,FacClarityExcellentPerc),
           (FacNavVeryPoorPerc,FacNavPoorPerc,FacNavAveragePerc,FacNavGoodPerc,FacNavExcellentPerc),
           (FacGHVeryPoorPerc,FacGHPoorPerc,FacGHAveragePerc,FacGHGoodPerc,FacGHExcellentPerc)]
  
Fac_stackratingdataperc = pd.DataFrame(Facpercent, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
Fac_stackratingdataperc.sort_index(inplace = True)

#create stacked percentage bar chart

fig, ax = plt.subplots()

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Aspects')
plt.title('Faculty Library Website Ratings by Percentage')
plt.grid()
Fac_stackratingdataperc.plot(kind='barh', color=['#033F63','#04578B','#0670B2','#0795ED','#40AEF2'], stacked=True,legend=False).set(title="Faculty Library Website Ratings by Percentage")
ax.set_xlim(xmin=0)
plt.xticks
plt.legend(bbox_to_anchor=(1.75, 1), loc='upper right', borderaxespad=0)
plt.savefig("Charts/facwebratings.png",bbox_inches='tight')

#Student Responses

#Clarity
StudentClarityRatings=StudentData['Clarity'].tolist
StudentClarityVeryPoor=0
StudentClarityPoor=0
StudentClarityAverage=0
StudentClarityGood=0
StudentClarityExcellent=0

for row in StudentClarityRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           StudentClarityVeryPoor=StudentClarityVeryPoor+1
       if 'Poor' in row:
           StudentClarityPoor=StudentClarityPoor+1
       if 'Average'in row:
           StudentClarityAverage=StudentClarityAverage+1
       if 'Good' in row:
           StudentClarityGood=StudentClarityGood+1
       if 'Excellent' in row:
           StudentClarityExcellent=StudentClarityExcellent+1

#convert to percentage
StudentCTotal=(StudentClarityVeryPoor)+(StudentClarityPoor)+(StudentClarityAverage)+(StudentClarityGood)+(StudentClarityExcellent)
StudentClarityVeryPoorPerc=(StudentClarityVeryPoor/StudentCTotal)*100
StudentClarityPoorPerc=(StudentClarityPoor/StudentCTotal)*100
StudentClarityAveragePerc=(StudentClarityAverage/StudentCTotal)*100
StudentClarityGoodPerc=(StudentClarityGood/StudentCTotal)*100
StudentClarityExcellentPerc=(StudentClarityExcellent/StudentCTotal)*100


#Navigation
StudentNavRatings=StudentData['Navigability'].tolist
StudentNavVeryPoor=0
StudentNavPoor=0
StudentNavAverage=0
StudentNavGood=0
StudentNavExcellent=0
for row in StudentNavRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           StudentNavVeryPoor=StudentNavVeryPoor+1
       if 'Poor' in row:
           StudentNavPoor=StudentNavPoor+1
       if 'Average'in row:
           StudentNavAverage=StudentNavAverage+1
       if 'Good' in row:
           StudentNavGood=StudentNavGood+1
       if 'Excellent' in row:
           StudentNavExcellent=StudentNavExcellent+1

#convert to percentage
StudentNavTotal=(StudentNavVeryPoor)+(StudentNavPoor)+(StudentNavAverage)+(StudentNavGood)+(StudentNavExcellent)
StudentNavVeryPoorPerc=(StudentNavVeryPoor/StudentNavTotal)*100
StudentNavPoorPerc=(StudentNavPoor/StudentNavTotal)*100
StudentNavAveragePerc=(StudentNavAverage/StudentNavTotal)*100
StudentNavGoodPerc=(StudentNavGood/StudentNavTotal)*100
StudentNavExcellentPerc=(StudentNavExcellent/StudentNavTotal)*100

#Get Help

StudentGHRatings=StudentData['Getting Help'].tolist
StudentGHVeryPoor=0
StudentGHPoor=0
StudentGHAverage=0
StudentGHGood=0
StudentGHExcellent=0
for row in StudentGHRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           StudentGHVeryPoor=StudentGHVeryPoor+1
       if 'Poor' in row:
           StudentGHPoor=StudentGHPoor+1
       if 'Average'in row:
           StudentGHAverage=StudentGHAverage+1
       if 'Good' in row:
           StudentGHGood=StudentGHGood+1
       if 'Excellent' in row:
           StudentGHExcellent=StudentGHExcellent+1

#convert to percentage
StudentGHTotal=(StudentGHVeryPoor)+(StudentGHPoor)+(StudentGHAverage)+(StudentGHGood)+(StudentGHExcellent)
StudentGHVeryPoorPerc=(StudentGHVeryPoor/StudentGHTotal)*100
StudentGHPoorPerc=(StudentGHPoor/StudentGHTotal)*100
StudentGHAveragePerc=(StudentGHAverage/StudentGHTotal)*100
StudentGHGoodPerc=(StudentGHGood/StudentGHTotal)*100
StudentGHExcellentPerc=(StudentGHExcellent/StudentGHTotal)*100

#Overall Rating

StudentRatings=StudentData['Overall'].tolist
StudentVeryPoor=0
StudentPoor=0
StudentAverage=0
StudentGood=0
StudentExcellent=0
for row in StudentRatings():
    if type(row) != float:
       if 'Very Poor' in row:  
           StudentVeryPoor=StudentVeryPoor+1
       if 'Poor' in row:
           StudentPoor=StudentPoor+1
       if 'Average'in row:
           StudentAverage=StudentAverage+1
       if 'Good' in row:
           StudentGood=StudentGood+1
       if 'Excellent' in row:
           StudentExcellent=StudentExcellent+1

#convert to percentage
StudentRatingTotal=(StudentVeryPoor)+(StudentPoor)+(StudentAverage)+(StudentGood)+(StudentExcellent)
StudentRatingVeryPoorPerc=(StudentVeryPoor/StudentRatingTotal)*100
StudentRatingPoorPerc=(StudentPoor/StudentRatingTotal)*100
StudentRatingAveragePerc=(StudentAverage/StudentRatingTotal)*100
StudentRatingGoodPerc=(StudentGood/StudentRatingTotal)*100
StudentRatingExcellentPerc=(StudentExcellent/StudentRatingTotal)*100

# Create DataFrame

StudentRatingdata = [( StudentVeryPoor,StudentPoor,StudentAverage,StudentGood,StudentExcellent),
           (StudentClarityVeryPoor,StudentClarityPoor,StudentClarityAverage,StudentClarityGood,StudentClarityExcellent),
           (StudentNavVeryPoor,StudentNavPoor,StudentNavAverage,StudentNavGood,StudentNavExcellent),
           (StudentGHVeryPoor,StudentGHPoor,StudentGHAverage,StudentGHGood,StudentGHExcellent)]
  
Student_stackratingdata = pd.DataFrame(StudentRatingdata, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
Student_stackratingdata.sort_index(inplace = True)
print(Student_stackratingdata)

#create percentage df

Studentpercent = [( StudentRatingVeryPoorPerc,StudentRatingPoorPerc,StudentRatingAveragePerc,StudentRatingGoodPerc,StudentRatingExcellentPerc),
           (StudentClarityVeryPoorPerc,StudentClarityPoorPerc,StudentClarityAveragePerc,StudentClarityGoodPerc,StudentClarityExcellentPerc),
           (StudentNavVeryPoorPerc,StudentNavPoorPerc,StudentNavAveragePerc,StudentNavGoodPerc,StudentNavExcellentPerc),
           (StudentGHVeryPoorPerc,StudentGHPoorPerc,StudentGHAveragePerc,StudentGHGoodPerc,StudentGHExcellentPerc)]
  
Student_stackratingdataperc = pd.DataFrame(Studentpercent, columns =['Very Poor','Poor','Average','Good','Excellent'],
                        index =[ 'Overall','Clarity','Navigability','Getting Help'])
  
# sort the rows of dataframe based on row index 
Student_stackratingdataperc.sort_index(inplace = True)

#create stacked percentage bar chart

fig, ax = plt.subplots()

ax.set_xlabel('Number of Respondents')
ax.set_ylabel('Aspects')
plt.title('Student Library Website Ratings by Percentage')
plt.grid()
Student_stackratingdataperc.plot(kind='barh', color=['#520000','#A30000','#F50000','#FF3333','#FF7070'], stacked=True,legend=False).set(title="Student Library Website Ratings by Percentage")
ax.set_xlim(xmin=0)
plt.xticks
plt.legend(bbox_to_anchor=(1.75, 1), loc='upper right', borderaxespad=0)
plt.savefig("Charts/studentwebratings.png",bbox_inches='tight')