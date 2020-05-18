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
