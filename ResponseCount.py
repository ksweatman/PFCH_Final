import csv
import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#return number of faculty and student responses
SurveyData=pandas.read_csv('SurveyData.csv')
ResponseCounts=SurveyData.groupby("Respondent_Type")['Respondent_Type'].count()

#return number of student responses by type
StudentData=pandas.read_csv('Student.csv')
StudentCounts=StudentData.groupby('Level')['Level'].count()

#define respondent type variables
Faculty_num=ResponseCounts[0]
CE_num=StudentCounts[0]
Grad_num=StudentCounts[1]
UG_num=StudentCounts[2]

#create pie chart of respondent types

plt.style.use('_mpl-gallery-nogrid')

x = [Faculty_num,UG_num,Grad_num,CE_num]
colors = ['DarkRed','Red','Tomato','LightSalmon']
Fac_patch = mpatches.Patch(color='DarkRed', label='Faculty')
UG_patch = mpatches.Patch(color='Red', label='Undergraduates')
Grad_patch = mpatches.Patch(color='Tomato', label='Graduate Students')
CE_patch = mpatches.Patch(color='LightSalmon', label='Continuing Education Students')


fig, ax = plt.subplots(figsize=(10,10))
ax.pie(x, colors=colors, autopct='%.1f%%', 
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)


ax.legend(handles=[Fac_patch,UG_patch,Grad_patch,CE_patch])        
ax.set_title('Survey Responses', fontsize=18, color='black')
plt.tight_layout()
plt.savefig("surveyresponses.png")