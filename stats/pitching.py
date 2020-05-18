import pandas as pd
import matplotlib.pyplot as plt
from data import games

#condense the data to just rows of type play
#games[] : shortcut to access the dataframe games
#check if the 'type' column's value equals 'play'
#select just the rows that have a 'type' of 'play'
#type is a column
plays = games[games['type'] == 'play']
#select all rows that contain 'K' in 'event' column
strike_outs = plays[plays['event'].str.contains('K')]
#group the strike_outs dataframe by year and then by game_id
strike_outs = strike_outs.groupby(['year','game_id']).size()
#strike_outs is now a groupby object. also contains a new column with number of strike outs in the game
#convert groupby object to a dataframe + name the column that was created
strike_outs = strike_outs.reset_index(name='strike_outs')
#converts the 2 selected columns values to numeric
strike_outs = strike_outs.loc[:,['year','strike_outs']].apply(pd.to_numeric)

strike_outs.plot(x='year',y='strike_outs',kind='scatter').legend(['Strike Outs'])
plt.show()
