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

#create pie chart based on student level status for all respondents
plt.style.use('_mpl-gallery-nogrid')
x = [304,265,229,28]
colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()