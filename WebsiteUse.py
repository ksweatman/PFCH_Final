import csv
import pandas as pd
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

# #bargraph
# fig = go.Figure(data=[go.Bar(
#     x=['To find out what technology is available for me to use', 'To find library hours', 'To reserve study space','To check on my loans','To get help from a library staff member','To find research materials','To find out about library locations','Other'], 
#     y=[WebUse1,WebUse2,WebUse3,WebUse4,WebUse5,WebUse6,WebUse7,WebUse8],
#     )])
# fig.show() 