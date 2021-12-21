import csv
import pandas 

#creates separate csvs for student and faculty respondents
data=pandas.read_csv('SurveyData.csv')
for (Respondent_Type), group in data.groupby(['Respondent_Type']):
    group.to_csv(f'{Respondent_Type}.csv', index=False)

#creates separate csvs for different student types
data=pandas.read_csv('Student.csv')
for (Level), group in data.groupby(['Level']):
    group.to_csv(f'{Level}.csv', index=False)


                