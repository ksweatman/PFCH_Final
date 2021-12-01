import csv
import pandas as pd
import re
import collections

word_count=[]

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

#Sample Question: "What feature(s) do you wish our website had?" in row [16]

with open ('SurveyData.csv','r') as CSVFile:
    word=(row[15], delimiter=" ")
    for row in CSVFile:
        if row[15]!=None:
            if word not in word_count:



print(words)
print(words_counted)
