import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#return number of faculty and student responses
SurveyData=pd.read_csv('SurveyData.csv')
ResponseCounts=SurveyData.groupby("Respondent_Type")['Respondent_Type'].count()

#return number of student responses by type
StudentData=pd.read_csv('Student.csv')
StudentCounts=StudentData.groupby('Level')['Level'].count()

#define respondent type variables
Faculty_num=ResponseCounts[0]
CE_num=StudentCounts[0]
Grad_num=StudentCounts[1]
UG_num=StudentCounts[2]

#create pie chart of respondent types

plt.style.use('_mpl-gallery-nogrid')

x = [Faculty_num,UG_num,Grad_num,CE_num]
colors = ['#A30000','#F50000','#FF3333','#FF7070']
Fac_patch = mpatches.Patch(color='#A30000', label='Faculty')
UG_patch = mpatches.Patch(color='#F50000', label='Undergraduates')
Grad_patch = mpatches.Patch(color='#FF3333', label='Graduate Students')
CE_patch = mpatches.Patch(color='#FF7070', label='Continuing Education Students')


fig, ax = plt.subplots(figsize=(10,10))
ax.pie(x, colors=colors, autopct='%.1f%%', 
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)


ax.legend(handles=[Fac_patch,UG_patch,Grad_patch,CE_patch])        
ax.set_title('Survey Responses', fontsize=18, color='black')
plt.tight_layout()
plt.savefig("Charts/surveyresponses.png")


#Question: Did you find what you were looking for?

Visit=SurveyData.groupby("On your last visit to the library website, did you find what you were looking for? - Selected Choice")["On your last visit to the library website, did you find what you were looking for? - Selected Choice"].count()

Yes=Visit[3]
No=Visit[2]
DontRemember=Visit[0]
DontUse=Visit[1]

#create pie chart

plt.style.use('_mpl-gallery-nogrid')

x = [Yes,No,DontRemember,DontUse]
labels=["Yes","No","Don't Remember","Don't Use Library Website"]

colors = ['#04578B','#0670B2','#0795ED','#40AEF2']
Yes_patch = mpatches.Patch(color='#04578B', label="Yes")
No_patch = mpatches.Patch(color='#0670B2', label="No")
DR_patch = mpatches.Patch(color='#0795ED', label="Don't Remember")
DontUse_patch = mpatches.Patch(color='#40AEF2', label="Don't Use Library Website")


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
plt.savefig("Charts/success.png")