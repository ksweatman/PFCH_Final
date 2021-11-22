import csv
import pandas 

data=pandas.read_csv('Student.csv')
for (Level), group in data.groupby(['Level']):
    group.to_csv(f'{Level}.csv', index=False)

print(pandas.read_csv("Graduate.csv"))
print(pandas.read_csv("Undergraduate.csv"))
print(pandas.read_csv("Continuing Education.csv"))

