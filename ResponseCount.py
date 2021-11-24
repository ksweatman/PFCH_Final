import csv
import pandas
import plotly.graph_objects as go

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
labels=['Faculty','Undergraduate Students','Graduate Students','Continuing Education Students']
values=[Faculty_num,UG_num,Grad_num,CE_num]
colors=['9d0000','e82e21','ff8664','ffb792']
fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
fig.show()