import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games["type"] == "play"] #select all rows that have a 'type' of 'play'
#label columns
plays.columns= ['type','inning','team','player','count','pitches','event','game_id','year']

#distribution of hits across innings. just need the hits,singles,doubles,triples,home runs
#select rows where the 'event' column's value starts with
    #S (not SB); D; T; HR
#only return 'inning' and 'event' columns
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning','event']]
#convert 'inning' column from strings to numbers
hits.loc[:,'inning'] = pd.to_numeric(hits.loc[:,'inning']) #all rows, 'inning' column only
#'event' column contains data: where the ball was hit,
    #and info not needed -> need to replace this with the type of hit

#create a dictionary called replacements
replacements = {r'^S(.*)' : 'single' ,
                r'^D(.*)' : 'double' ,
                r'^T(.*)' : 'triple' ,
                r'^HR(.*)' : 'hr' }
hit_type = hits['event'].replace(replacements,regex=True)
#add a new column with assign() with new column name and new column
hits = hits.assign(hit_type=hit_type)
#group by inning and hit type
#call size() to count the number of hits per inning
#reset the index of the resulting dataframe, name newly created column 'count'
hits = hits.groupby(['inning','hit_type']).size().reset_index(name='count')

#there are only 4 types of hits, save some memory
    #by converting column 'hit_type' to a categorical column
hits['hit_type'] = pd.Categorical(hits['hit_type'] , ['single','double','triple','hr'])
#sort values by 'inning' and 'hit_type'
hits = hits.sort_values(['inning','hit_type'])

#reshape before plotting
hits = hits.pivot(index='inning',columns='hit_type',values='count')
#stacked bar chart
hits.plot.bar(stacked=True)
plt.show()
