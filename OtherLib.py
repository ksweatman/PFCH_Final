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
colors = ['#52256A','#C20114','#028090','#7EE081','#D14081','#F6AE2D','#313B72']
sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(10,10))

ax.set_xlabel('Library')
ax.set_ylabel('Responses')
plt.title('What other library websites do you visit?')
plt.grid()
bar_plot = sns.barplot(x, y, ax=ax)
ax.set_xlim(xmin=0)
plt.xticks
plt.tight_layout()
plt.savefig("Charts/libsites.png")

#Count reasons for using other libraries

#NYPL
NYPLList=SurveyData['NYPL Use'].tolist()
NYPLUse1=0
NYPLUse2=0
NYPLUse3=0
NYPLUse4=0
NYPLUse5=0
NYPLUse6=0
NYPLUse7=0
NYPLUse8=0
for row in NYPLList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           NYPLUse1=NYPLUse1+1
       if 'To find library hours' in row:
           NYPLUse2=NYPLUse2+1
       if 'To find out about library locations'in row:
           NYPLUse3=NYPLUse3+1
       if 'To reserve study space' in row:
           NYPLUse4=NYPLUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           NYPLUse5=NYPLUse5+1
       if 'To get help from a library staff member' in row:
           NYPLUse6=NYPLUse6+1
       if 'To find research materials' in row:
           NYPLUse7=NYPLUse7+1
       if 'Other' in row:
           NYPLUse8=NYPLUse8+1
#create list of "Other" responses
NYPLListOther=[]
for row in SurveyData['NYPL Use Other']:
    if type(row) != float:
        NYPLListOther.append(row)
print(NYPLListOther)

#BPL

BPLList=SurveyData['BPL Use'].tolist()
BPLUse1=0
BPLUse2=0
BPLUse3=0
BPLUse4=0
BPLUse5=0
BPLUse6=0
BPLUse7=0
BPLUse8=0
for row in BPLList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           BPLUse1=BPLUse1+1
       if 'To find library hours' in row:
           BPLUse2=BPLUse2+1
       if 'To find out about library locations'in row:
           BPLUse3=BPLUse3+1
       if 'To reserve study space' in row:
           BPLUse4=BPLUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           BPLUse5=BPLUse5+1
       if 'To get help from a library staff member' in row:
           BPLUse6=BPLUse6+1
       if 'To find research materials' in row:
           BPLUse7=BPLUse7+1
       if 'Other' in row:
           BPLUse8=BPLUse8+1
#create list of "Other" responses
BPLListOther=[]
for row in SurveyData['BPL Use Other']:
    if type(row) != float:
        BPLListOther.append(row)
print(BPLListOther)

#QPL

QPLList=SurveyData['QPL Use'].tolist()
QPLUse1=0
QPLUse2=0
QPLUse3=0
QPLUse4=0
QPLUse5=0
QPLUse6=0
QPLUse7=0
QPLUse8=0
for row in QPLList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           QPLUse1=QPLUse1+1
       if 'To find library hours' in row:
           QPLUse2=QPLUse2+1
       if 'To find out about library locations'in row:
           QPLUse3=QPLUse3+1
       if 'To reserve study space' in row:
           QPLUse4=QPLUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           QPLUse5=QPLUse5+1
       if 'To get help from a library staff member' in row:
           QPLUse6=QPLUse6+1
       if 'To find research materials' in row:
           QPLUse7=QPLUse7+1
       if 'Other' in row:
           QPLUse8=QPLUse8+1
#create list of "Other" responses
QPLListOther=[]
for row in SurveyData['QPL Use Other']:
    if type(row) != float:
        QPLListOther.append(row)
print(QPLListOther)

#NYU

NYUList=SurveyData['NYU Use'].tolist()
NYUUse1=0
NYUUse2=0
NYUUse3=0
NYUUse4=0
NYUUse5=0
NYUUse6=0
NYUUse7=0
NYUUse8=0
for row in NYUList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           NYUUse1=NYUUse1+1
       if 'To find library hours' in row:
           NYUUse2=NYUUse2+1
       if 'To find out about library locations'in row:
           NYUUse3=NYUUse3+1
       if 'To reserve study space' in row:
           NYUUse4=NYUUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           NYUUse5=NYUUse5+1
       if 'To get help from a library staff member' in row:
           NYUUse6=NYUUse6+1
       if 'To find research materials' in row:
           NYUUse7=NYUUse7+1
       if 'Other' in row:
           NYUUse8=NYUUse8+1
#create list of "Other" responses
NYUListOther=[]
for row in SurveyData['NYU Use Other']:
    if type(row) != float:
        NYUListOther.append(row)
print(NYUListOther)

#Cooper Union

CUList=SurveyData['Cooper Union Use'].tolist()
CUUse1=0
CUUse2=0
CUUse3=0
CUUse4=0
CUUse5=0
CUUse6=0
CUUse7=0
CUUse8=0
for row in CUList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           CUUse1=CUUse1+1
       if 'To find library hours' in row:
           CUUse2=CUUse2+1
       if 'To find out about library locations'in row:
           CUUse3=CUUse3+1
       if 'To reserve study space' in row:
           CUUse4=CUUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           CUUse5=CUUse5+1
       if 'To get help from a library staff member' in row:
           CUUse6=CUUse6+1
       if 'To find research materials' in row:
           CUUse7=CUUse7+1
       if 'Other' in row:
           CUUse8=CUUse8+1
#create list of "Other" responses
CUListOther=[]
for row in SurveyData['Cooper Union Use Other']:
    if type(row) != float:
        CUListOther.append(row)
print(CUListOther)

#Other

#Cooper Union

OtherList=SurveyData['Other Use'].tolist()
OtherUse1=0
OtherUse2=0
OtherUse3=0
OtherUse4=0
OtherUse5=0
OtherUse6=0
OtherUse7=0
OtherUse8=0
for row in OtherList:
    if type(row) != float:
       if 'To find out what technology is available for me to use' in row:  
           OtherUse1=OtherUse1+1
       if 'To find library hours' in row:
           OtherUse2=OtherUse2+1
       if 'To find out about library locations'in row:
           OtherUse3=OtherUse3+1
       if 'To reserve study space' in row:
           OtherUse4=OtherUse4+1
       if 'To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)' in row:
           OtherUse5=OtherUse5+1
       if 'To get help from a library staff member' in row:
           OtherUse6=OtherUse6+1
       if 'To find research materials' in row:
           OtherUse7=OtherUse7+1
       if 'Other' in row:
           OtherUse8=OtherUse8+1
#create list of "Other" responses
OtherListOther=[]
for row in SurveyData['Other Use Other']:
    if type(row) != float:
        OtherListOther.append(row)
print(OtherListOther)

# Create DataFrame
usedata = {'OtherLibUses':['Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other','Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other','Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other','Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other','Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other','Available Technology','Library Hours','Library Locations','Book Space','Check on Loans','Get Help from Library Staff','Find Research Materials','Other'],
        'Library':['NYPL','NYPL','NYPL','NYPL','NYPL','NYPL','NYPL','NYPL','BPL','BPL','BPL','BPL','BPL','BPL','BPL','BPL','QPL','QPL','QPL','QPL','QPL','QPL','QPL','QPL','NYU','NYU','NYU','NYU','NYU','NYU','NYU','NYU','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Other','Other','Other','Other','Other','Other','Other','Other'],
        'OtherLibUseResponses':[NYPLUse1,NYPLUse2,NYPLUse3,NYPLUse4,NYPLUse5,NYPLUse6,NYPLUse7,NYPLUse8,BPLUse1,BPLUse2,BPLUse3,BPLUse4,BPLUse5,BPLUse6,BPLUse7,BPLUse8,QPLUse1,QPLUse2,QPLUse3,QPLUse4,QPLUse5,QPLUse6,QPLUse7,QPLUse8,NYUUse1,NYUUse2,NYUUse3,NYUUse4,NYUUse5,NYUUse6,NYUUse7,NYUUse8,CUUse1,CUUse2,CUUse3,CUUse4,CUUse5,CUUse6,CUUse7,CUUse8,OtherUse1,OtherUse2,OtherUse3,OtherUse4,OtherUse5,OtherUse6,OtherUse7,OtherUse8]
}

usedf = pd.DataFrame(usedata)
usedf.pivot(index="Library", columns="OtherLibUses", values="OtherLibUseResponses")

#Grouped Bar Plot
colors = ['#52256A','#C20114','#028090','#7EE081','#D14081','#F6AE2D']
sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(10,10))
plt.grid()
bar_plot = sns.barplot(
    x="OtherLibUses", 
    y="OtherLibUseResponses", 
    hue="Library", 
    data=usedf, 
    ci=None
    )
ax.set_title('What Do You Use Other Library Sites For?')
ax.set_ylabel('Responses')
ax.set_xlabel('Uses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/otherlibuse.png") 

#Count likes about other libraries

#NYPL
NYPLLikeList=SurveyData['NYPL Like'].tolist()
NYPLLike1=0
NYPLLike2=0
NYPLLike3=0
NYPLLike4=0
for row in NYPLLikeList:
    if type(row) != float:
       if 'The site is easy to navigate' in row:  
           NYPLLike1=NYPLLike1+1
       if 'The site is well-written with clear information' in row:
           NYPLLike2=NYPLLike2+1
       if 'It is easy to get help from a staff member if I need it'in row:
           NYPLLike3=NYPLLike3+1
       if 'Other' in row:
           NYPLLike4=NYPLLike4+1
#create list of "Other" responses
NYPLLikeListOther=[]
for row in SurveyData['NYPL Like Other']:
    if type(row) != float:
        NYPLLikeListOther.append(row)
print(NYPLLikeListOther)

#BPL

BPLLikeList=SurveyData['BPL Like'].tolist()
BPLLike1=0
BPLLike2=0
BPLLike3=0
BPLLike4=0
for row in BPLLikeList:
    if type(row) != float:
        if 'The site is easy to navigate' in row:  
           BPLLike1=BPLLike1+1
        if 'The site is well-written with clear information' in row:
           BPLLike2=BPLLike2+1
        if 'It is easy to get help from a staff member if I need it'in row:
           BPLLike3=BPLLike3+1
        if 'Other' in row:
           BPLLike4=BPLLike4+1
#create list of "Other" responses
BPLLikeListOther=[]
for row in SurveyData['BPL Like Other']:
    if type(row) != float:
        BPLLikeListOther.append(row)
print(BPLLikeListOther)

#QPL

QPLLikeList=SurveyData['QPL Like'].tolist()
QPLLike1=0
QPLLike2=0
QPLLike3=0
QPLLike4=0
for row in QPLLikeList:
    if type(row) != float:
        if 'The site is easy to navigate' in row:  
           QPLLike1=QPLLike1+1
        if 'The site is well-written with clear information' in row:
           QPLLike2=QPLLike2+1
        if 'It is easy to get help from a staff member if I need it'in row:
           QPLLike3=QPLLike3+1
        if 'Other' in row:
           QPLLike4=QPLLike4+1
#create list of "Other" responses
QPLLikeListOther=[]
for row in SurveyData['QPL Like Other']:
    if type(row) != float:
        QPLLikeListOther.append(row)
print(QPLLikeListOther)

#NYU

NYULikeList=SurveyData['NYU Like'].tolist()
NYULike1=0
NYULike2=0
NYULike3=0
NYULike4=0
for row in NYULikeList:
    if type(row) != float:
        if 'The site is easy to navigate' in row:  
           NYULike1=NYULike1+1
        if 'The site is well-written with clear information' in row:
           NYULike2=NYULike2+1
        if 'It is easy to get help from a staff member if I need it'in row:
           NYULike3=NYULike3+1
        if 'Other' in row:
           NYULike4=NYULike4+1
#create list of "Other" responses
NYULikeListOther=[]
for row in SurveyData['NYU Like Other']:
    if type(row) != float:
        NYULikeListOther.append(row)
print(NYULikeListOther)

#Cooper Union

CULikeList=SurveyData['Cooper Union Like'].tolist()
CULike1=0
CULike2=0
CULike3=0
CULike4=0
CULike5=0
CULike6=0
CULike7=0
CULike8=0
for row in CULikeList:
    if type(row) != float:
        if 'The site is easy to navigate' in row:  
           CULike1=CULike1+1
        if 'The site is well-written with clear information' in row:
           CULike2=CULike2+1
        if 'It is easy to get help from a staff member if I need it'in row:
           CULike3=CULike3+1
        if 'Other' in row:
           CULike4=CULike4+1
#create list of "Other" responses
CULikeListOther=[]
for row in SurveyData['Cooper Union Like Other']:
    if type(row) != float:
        CULikeListOther.append(row)
print(CULikeListOther)

#Other

#Cooper Union

OtherLikeList=SurveyData['Other Like'].tolist()
OtherLike1=0
OtherLike2=0
OtherLike3=0
OtherLike4=0
for row in OtherLikeList:
    if type(row) != float:
        if 'The site is easy to navigate' in row:  
           OtherLike1=OtherLike1+1
        if 'The site is well-written with clear information' in row:
           OtherLike2=OtherLike2+1
        if 'It is easy to get help from a staff member if I need it'in row:
           OtherLike3=OtherLike3+1
        if 'Other' in row:
           OtherLike4=OtherLike4+1
#create list of "Other" responses
OtherLikeListOther=[]
for row in SurveyData['Other Like Other']:
    if type(row) != float:
        OtherLikeListOther.append(row)
print(OtherLikeListOther)

# Create DataFrame
likedata = {'OtherLibLikes':['Easy to Navigate','Clearly Written','Easy to Get Help','Other','Easy to Navigate','Clearly Written','Easy to Get Help','Other','Easy to Navigate','Clearly Written','Easy to Get Help','Other','Easy to Navigate','Clearly Written','Easy to Get Help','Other','Easy to Navigate','Clearly Written','Easy to Get Help','Other','Easy to Navigate','Clearly Written','Easy to Get Help','Other'],
        'Library':['NYPL','NYPL','NYPL','NYPL','BPL','BPL','BPL','BPL','QPL','QPL','QPL','QPL','NYU','NYU','NYU','NYU','Cooper Union','Cooper Union','Cooper Union','Cooper Union','Other','Other','Other','Other'],
        'OtherLibLikeResponses':[NYPLLike1,NYPLLike2,NYPLLike3,NYPLLike4,BPLLike1,BPLLike2,BPLLike3,BPLLike4,QPLLike1,QPLLike2,QPLLike3,QPLLike4,NYULike1,NYULike2,NYULike3,NYULike4,CULike1,CULike2,CULike3,CULike4,OtherLike1,OtherLike2,OtherLike3,OtherLike4]
}

likedf = pd.DataFrame(likedata)
likedf.pivot(index="Library", columns="OtherLibLikes", values="OtherLibLikeResponses")

#Grouped Bar Plot
colors = ['#52256A','#C20114','#028090','#7EE081','#D14081','#F6AE2D']
sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(10,10))
plt.grid()
bar_plot = sns.barplot(
    x="OtherLibLikes", 
    y="OtherLibLikeResponses", 
    hue="Library", 
    data=likedf, 
    ci=None
    )
ax.set_title('What Do You Like About Other Library Sites?')
ax.set_ylabel('Responses')
ax.set_xlabel('Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Charts/otherliblike.png") 