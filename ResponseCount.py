import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

#return number of faculty and student responses
SurveyData=pandas.read_csv('SurveyData.csv')
ResponseCounts=SurveyData.groupby("Respondent_Type")['Respondent_Type'].count()
print(ResponseCounts)

#return number of student responses by type
StudentData=pandas.read_csv('Student.csv')
StudentCounts=StudentData.groupby('Level')['Level'].count()
print(StudentCounts)

 #calculate and return percentages of respondents by type
FacultyPercent=round((((ResponseCounts[0])/len(SurveyData.index))*100))
CEPercent=round((((StudentCounts[0])/len(SurveyData.index))*100))
GradPercent=round((((StudentCounts[1])/len(SurveyData.index))*100))
UGPercent=round((((StudentCounts[2])/len(SurveyData.index))*100))

print('Faculty:'+ str(FacultyPercent)+'%')
print('Graduate Students:'+ str(GradPercent)+'%')
print('Undergraduate Students:'+ str(UGPercent)+'%')
print('Continuing Education Students:'+ str(CEPercent)+'%')

#create pie chart of respondent types
plt.style.use('_mpl-gallery-nogrid')
x = [FacultyPercent,UGPercent,GradPercent,CEPercent]
colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()