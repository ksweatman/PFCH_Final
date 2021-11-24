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
LibFreq=SurveyData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()

WebFreq=SurveyData.groupby("How often do you currently visit the library website?")['How often do you currently visit the library website?'].count()


#Faculty Responses
FacLibFreq=FacData.groupby("How often do you currently visit the library in person?")['How often do you currently visit the library in person?'].count()
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

#Return results as stacked, grouped bar graph