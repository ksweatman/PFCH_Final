import csv
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

WebUse1=pd.Series(SurveyData['Web Uses']).str.extractall("(To find out what technology is available for me to use)").count()
print(WebUse1)
WebUse2=pd.Series(SurveyData['Web Uses']).str.extractall("(To find library hours)").count()
print(WebUse2)
WebUse3=pd.Series(SurveyData['Web Uses']).str.extractall("(To reserve study space)").count()
print(WebUse3)
WebUse4=pd.Series(SurveyData['Web Uses']).str.extractall("(To check on my loans)").count()
print(WebUse4)
WebUse5=pd.Series(SurveyData['Web Uses']).str.extractall("(To get help from a library staff member)").count()
print(WebUse5)
WebUse6=pd.Series(SurveyData['Web Uses']).str.extractall("(To find research materials)").count()
print(WebUse6)
WebUse7=pd.Series(SurveyData['Web Uses']).str.extractall("(To find out about library locations)").count()
print(WebUse7)
WebUse8=pd.Series(SurveyData['Web Uses']).str.extractall("(Other)").count()
print(WebUse8)

""" #bar graph
#matplotlib

data = [WebUse1,WebUse2,WebUse3,WebUse4,WebUse5,WebUse6,WebUse7,WebUse8]
labels = ['To find out what technology is available for me to use', 'To find library hours', 'To reserve study space','To check on my loans','To get help from a library staff member','To find research materials','To find out about library locations','Other']
def f(x):
    return np.int(x)
f2 = np.vectorize(f)
x = np.arange([WebUse1,WebUse2,WebUse3,WebUse4,WebUse5,WebUse6,WebUse7,WebUse8])
plt.plot(x, f2(x))
plt.xticks(range(len(data)), labels)
plt.xlabel('Website Uses')
plt.ylabel('# of Respondents')
plt.title('Why do you use the library website?')
plt.bar(range(len(data)), data) 

plt.show()

#plotly go
uses=['To find out what technology is available for me to use', 'To find library hours', 'To reserve study space','To check on my loans','To get help from a library staff member','To find research materials','To find out about library locations','Other']
fig = go.Figure([go.Bar(
    x=uses, 
    y=[WebUse1,WebUse2,WebUse3,WebUse4,WebUse5,WebUse6,WebUse7,WebUse8],
    )])
fig.show()"""