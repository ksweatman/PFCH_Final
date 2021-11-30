import csv
import pandas as pd

#load datasets
SurveyData=pd.read_csv('SurveyData.csv')
FacData=pd.read_csv('Faculty.csv')
StudentData=pd.read_csv('Student.csv')
GradData=pd.read_csv('Graduate.csv')
UGData=pd.read_csv('Undergraduate.csv')

#Single Answers-Did you find what you were looking for?
Answer=SurveyData.groupby("On your last visit to the library website, did you find what you were looking for? - Selected Choice")['On your last visit to the library website, did you find what you were looking for? - Selected Choice'].count()
print(Answer)

#Multiple Answers-What other library websites do you use?

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