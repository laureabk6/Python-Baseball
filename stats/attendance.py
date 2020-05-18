#test module locally: open terminal at root of project
# pytest -k module2

import pandas as pd
import matplotlib.pyplot as plt
from data import games #from file data.py import games dataframe

#games contains the attendance for each game
#type multi2 multi3 ... year
#info attendance 4522 ... 1946
#select rows with info and attendance and only the year and multi3 columns
attendance = games.loc[(games['type'] == 'info') & (games['multi2']=='attendance'),['year','multi3']]
#change column labels
attendance.columns = ['year','attendance']

#select all rows, but just the attendance column
#converts the attendance values from string to numerical values
attendance.loc[:,'attendance'] = pd.to_numeric(attendance.loc[:,'attendance'])

attendance.plot(x='year',y='attendance',figsize=(15,7),kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
#dahsed green line perpendicular to the x-axis, at the mean (parallel to y axis)
plt.axhline(y=attendance['attendance'].mean(),label='Mean',linestyle='--',color='green')
plt.show()
