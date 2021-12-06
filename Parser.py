import csv
import pandas as pd

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

#Single Answers-Did you find what you were looking for?-pie chart
Answer=SurveyData.groupby("On your last visit to the library website, did you find what you were looking for? - Selected Choice")['On your last visit to the library website, did you find what you were looking for? - Selected Choice'].count()
print(Answer)

#Multiple Answers-What other library websites do you use?-bar graph

NYPL=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(New York Public Library)").count()
print(NYPL)
BPL=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(Brooklyn Public Library)").count()
print(BPL)
QPL=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(Queens Public Library)").count()
print(QPL)
NYU=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(NYU)").count()
print(NYU)
CooperUnion=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(Cooper Union)").count()
print(CooperUnion)
Other=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(Other)").count()
print(Other)
NA=pd.Series(SurveyData['What other library websites do you visit? - Selected Choice']).str.extractall("(None/Not Applicable)").count()
print(NA)

#Site Ratings-graph as stacked percentage bar chart

Clarity_Rating=SurveyData.groupby("Rate the following aspects of the website - Information Clarity")['Rate the following aspects of the website - Information Clarity'].count()
Clarity_Rating_Perc=(Clarity_Rating/len(SurveyData))*100
Nav_Rating=SurveyData.groupby("Rate the following aspects of the website - Navigability")['Rate the following aspects of the website - Navigability'].count()
Nav_Rating_Perc=(Nav_Rating/len(SurveyData))*100
GetHelp_Rating=SurveyData.groupby("Rate the following aspects of the website - Getting Help")['Rate the following aspects of the website - Getting Help'].count()
GetHelp_Rating_Perc=(GetHelp_Rating/len(SurveyData))*100
Rating=SurveyData.groupby("Rate the following aspects of the website - Overall Experience")['Rate the following aspects of the website - Overall Experience'].count()
Rating_Perc=(Rating/len(SurveyData))*100