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
       if 'Multiple visits per day' in row:  
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

#bar plot-library vs. web use frequency

#Student Responses

StudentLibFreqs=StudentData['Library Use Frequency'].tolist()
StudentWebFreqs=StudentData['Web Use Frequency'].tolist()

StudentWebFreq1=0
StudentWebFreq2=0
StudentWebFreq3=0
StudentWebFreq4=0
StudentWebFreq5=0
StudentWebFreq6=0
StudentWebFreq7=0

for row in StudentWebFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           StudentWebFreq1=StudentWebFreq1+1
       if 'Once a day' in row:
           StudentWebFreq2=StudentWebFreq2+1
       if'2-3 times per week'in row:
           StudentWebFreq3=StudentWebFreq3+1
       if 'Once a week' in row:
           StudentWebFreq4=StudentWebFreq4+1
       if '2-3 times per month' in row:
           StudentWebFreq5=StudentWebFreq5+1
       if 'Once per semester' in row:
           StudentWebFreq6=StudentWebFreq6+1
       if 'Never' in row:
           StudentWebFreq7=StudentWebFreq7+1


StudentLibFreq1=0
StudentLibFreq2=0
StudentLibFreq3=0
StudentLibFreq4=0
StudentLibFreq5=0
StudentLibFreq6=0
StudentLibFreq7=0

for row in StudentLibFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           StudentLibFreq1=StudentLibFreq1+1
       if 'Once a day' in row:
           StudentLibFreq2=StudentLibFreq2+1
       if'2-3 times per week'in row:
           StudentLibFreq3=StudentLibFreq3+1
       if 'Once a week' in row:
           StudentLibFreq4=StudentLibFreq4+1
       if '2-3 times per month' in row:
           StudentLibFreq5=StudentLibFreq5+1
       if 'Once per semester' in row:
           StudentLibFreq6=StudentLibFreq6+1
       if 'Never' in row:
           StudentLibFreq7=StudentLibFreq7+1

#Faculty Responses

FacLibFreqs=FacData['Library Use Frequency'].tolist()
FacWebFreqs=FacData['Web Use Frequency'].tolist()

FacWebFreq1=0
FacWebFreq2=0
FacWebFreq3=0
FacWebFreq4=0
FacWebFreq5=0
FacWebFreq6=0
FacWebFreq7=0

for row in FacWebFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           FacWebFreq1=FacWebFreq1+1
       if 'Once a day' in row:
           FacWebFreq2=FacWebFreq2+1
       if'2-3 times per week'in row:
           FacWebFreq3=FacWebFreq3+1
       if 'Once a week' in row:
           FacWebFreq4=FacWebFreq4+1
       if '2-3 times per month' in row:
           FacWebFreq5=FacWebFreq5+1
       if 'Once per semester' in row:
           FacWebFreq6=FacWebFreq6+1
       if 'Never' in row:
           FacWebFreq7=FacWebFreq7+1


FacLibFreq1=0
FacLibFreq2=0
FacLibFreq3=0
FacLibFreq4=0
FacLibFreq5=0
FacLibFreq6=0
FacLibFreq7=0

for row in FacLibFreqs:
    if type(row) != float:
       if 'Multiple visits per day' in row:  
           FacLibFreq1=FacLibFreq1+1
       if 'Once a day' in row:
           FacLibFreq2=FacLibFreq2+1
       if'2-3 times per week'in row:
           FacLibFreq3=FacLibFreq3+1
       if 'Once a week' in row:
           FacLibFreq4=FacLibFreq4+1
       if '2-3 times per month' in row:
           FacLibFreq5=FacLibFreq5+1
       if 'Once per semester' in row:
           FacLibFreq6=FacLibFreq6+1
       if 'Never' in row:
           FacLibFreq7=FacLibFreq7+1



#Undergrad Responses


#Graduate Responses


#Return results as grouped bar graph
# Library/Web Use Grouped together, graphs for faculty, then students
# """