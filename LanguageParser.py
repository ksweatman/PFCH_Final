import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

#Sample Question: "What feature(s) do you wish our website had?" in row [15]
words=[]
with open ('SurveyData.csv','r') as CSVFile:
    for row in CSVFile:
        csv_words=row[15].split(" ")
        for i in csv_words:
            words.append(i)
word_count=[]
for i in words:
    x=words.count(i)
    word_count.append((i,x))
"""   if word not in word_count:
            word_count[word]=0
        word_count[word]=word_count[word]+1 """

print(word_count)

#word_count=pd.Series(SurveyData["What feature(s) do you wish our website had?"]).str.extractall(r'*\w').count()
#print(word_count)