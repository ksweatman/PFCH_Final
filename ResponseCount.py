import csv
import pandas
import matplotlib.pyplot as plt
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
labels=['Faculty','Undergraduate Students','Graduate Students','Continuing Education Students']
colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))


fig, ax = plt.subplots(figsize=(10,10))
ax.pie(x, colors=colors, labels=labels,autopct='%.1f%%', 
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)

"""ax.legend(labels,x,
          title="Respondents",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))"""
          
ax.set_title('Survey Responses', fontsize=18, color='black')
plt.tight_layout()
plt.savefig("surveyresponses.png")



"""plotly code
values=[]
colors=['9d0000','e82e21','ff8664','ffb792']
fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
fig.show()"""