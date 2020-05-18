import pandas as pd
import matplotlib.pyplot as plt
#what is the defensive efficiency ration by league, since 1978
from frames import games, info, events

#query function to select all rows of 'games' dataframe
    #that have a 'type' of 'play' but do NOT have 'NP' as 'event'
plays = games.query(" type == 'play' & event != 'NP' ")
#adjust/rename column labels
plays.columns = ['type','inning','team','player','count','pitches',
                 'event','game_id','year']

#remove consecutive duplicate rows that represent the same at bat
    #shift() moves the index a specified amount up or down
#select all Rows that do Not match a consecutive row in the player column
#keep only a few specified columns
pa = plays.loc[plays['player'].shift() != plays['player'] ,
               ['year','game_id','inning','team','player']]

#on groupby() chain, a call to size() to count this appearance
    #reset_index() passing in the right keyword argument to name the newly created column
pa = pa.groupby(['year','game_id','team']).size().reset_index(name='PA')

#reshape the data by the type of event
#adjust the index -> set_index()
#the event types need to be the columns of our dataframe -> unstack()
events = events.set_index(['year','game_id','team','event_type'])
events = events.unstack().fillna(0).reset_index()
#after unstacking, it will have multiple levels of column labels
    #use droplevel() to remove one level
events.columns = events.columns.droplevel()
#change the column labels
events.columns = ['year','game_id','team','BB','E','H','HBP','HR','ROE','SO']
#remove label of the index using rename_axis(): pass in label of None, on the column axis
events = events.rename_axis(None,axis='columns')

#pa dataframe has columns year, game_id, team, PA
#events dataframe has year, game_id, team, and a column for every event_type
#merge them together with pd.merge()
    #columns to merge: year, game_id, team
events_plus_pa = pd.merge(events,pa, how='outer', left_on=['year','game_id','team'],
                          right_on=['year','game_id','team'])
defense = pd.merge(events_plus_pa,info) #info: home team vs visiting team
#calculate the DER of each team
defense.loc[:,'DER'] = 1 - ((defense['H']+defense['ROE'])/(defense['PA']-defense['BB']-defense['SO']-defense['HBP']-defense['HR']))
#convert the year column to numeric values
defense.loc[:,'year'] = pd.to_numeric(defense['year'])

#plot the DER of the all-star teams in the last 40 years
#select rows with year>1978 and also only keep certain columns
der = defense.loc[defense['year'] >= 1978, ['year','defense','DER']]
#call pivot to adjust the data for plotting
der = der.pivot(index='year',columns='defense',values='DER')
der.plot(x_compat=True,xticks=range(1978,2018,4),rot=45)
plt.show()
