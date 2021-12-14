import csv
import pandas
import plotly.graph_objects as go

#load datasets
SurveyData=pandas.read_csv('SurveyData.csv')
FacData=pandas.read_csv('Faculty.csv')
StudentData=pandas.read_csv('Student.csv')
GradData=pandas.read_csv('Graduate.csv')
UGData=pandas.read_csv('Undergraduate.csv')

#return responses to first 2 survey questions

#Overall Responses

LibFreqs=SurveyData['Library Use Frequency'].tolist()
WebFreqs=SurveyData['Web Use Frequency'].tolist()

WebFreq1=0
WebFreq2=0
WebFreq3=0
WebFreq4=0
WebFreq5=0
WebFreq6=0
WebFreq7=0

for row in WebFreqs:
    if type(row) != float:
       if 'Multiple visits for day' in row:  
           WebFreq1=WebFreq1+1
       if 'Once a day' in row:
           WebFreq2=WebFreq2+1
       if'2-3 times per week'in row:
           WebFreq3=WebFreq3+1
       if 'Once a week' in row:
           WebFreq4=WebFreq4+1
       if '2-3 times per month' in row:
           WebFreq5=WebFreq5+1
       if 'Once per semester' in row:
           WebFreq6=WebFreq6+1
       if 'Never' in row:
           WebFreq7=WebFreq7+1


LibFreq1=0
LibFreq2=0
LibFreq3=0
LibFreq4=0
LibFreq5=0
LibFreq6=0
LibFreq7=0

for row in LibFreqs:
    if type(row) != float:
       if 'Multiple visits for day' in row:  
           LibFreq1=LibFreq1+1
       if 'Once a day' in row:
           LibFreq2=LibFreq2+1
       if'2-3 times per week'in row:
           LibFreq3=LibFreq3+1
       if 'Once a week' in row:
           LibFreq4=LibFreq4+1
       if '2-3 times per month' in row:
           LibFreq5=LibFreq5+1
       if 'Once per semester' in row:
           LibFreq6=LibFreq6+1
       if 'Never' in row:
           LibFreq7=LibFreq7+1



#Faculty Responses
"""FacLibFreq=FacData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()
FacWebFreq=FacData.groupby("How often do you currently visit the library website?")['How often do you currently visit the library website?'].count()
#print ('Faculty In-Person Use:'+str(FacLibFreq))
#print ('Faculty Website Use:'+str(FacWebFreq))

#Student Responses
StudentLibFreq=StudentData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()
StudentWebFreq=StudentData.groupby("How often do you currently visit the library website?")['How often do you currently visit the library website?'].count()
#print('Student In-Person Use:'+str(StudentLibFreq))
#print('Student Website Use:'+str(StudentWebFreq))

#Undergrad Responses
UGLibFreq=UGData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()
UGWebFreq=UGData.groupby("How often do you currently visit the library website?")['How often do you currently visit the library website?'].count()
#print('Undergrad In-Person Use:'+str(UGLibFreq))
#print('Undergrad Website Use:'+str(UGWebFreq))

#Graduate Responses
GradLibFreq=GradData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()
GradWebFreq=GradData.groupby("How often do you currently visit the library website?")['How often do you currently visit the library website?'].count()
#print('Grad Student In-Person Use:'+str(GradLibFreq))
#print('Grad Student Website Use:'+str(GradWebFreq))

#Return results as grouped bar graph
# Library/Web Use Grouped together, graphs for faculty, then students
# """