import csv
import pandas 

data=pandas.read_csv('SurveyData.csv')
for (Respondent_Type), group in data.groupby(['Respondent_Type']):
    group.to_csv(f'{Respondent_Type}.csv', index=False)

print(pandas.read_csv("Instructional Staff.csv"))
print(pandas.read_csv("Student.csv"))


                