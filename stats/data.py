import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
#game_files contain a list of all name files that end with .EVE in the games folder
game_files.sort()

game_frames = [] #empty list

for game_file in game_files:
    game_frame = pd.read_csv(game_file,names = ['type','multi2','multi3','multi4','multi5','multi6','event'])
    game_frames.append(game_frame)

games = pd.concat(game_frames) #large dataframe called games
games.loc[games['multi5'] == '??' , ['multi5']] = ''

identifiers = games["multi2"].str.extract(r'(.LS(\d{4})\d{5})') #is a dataframe
#has 2 columns. for rows that match the regex, the row has the correct extracted values
identifiers = identifiers.fillna(method='ffill')#values must be filled in for all rows

identifiers.columns=["game_id","year"])#change column labels
# games = pd.concat([games,identifiers],axis=1,sort=False)#concatenate identifier columns:
# #append the columns of identifiers to games
# games = games.fillna(' ')#fill Nan values
#
# #reduce memory used by games, provide Pandas with clue to what data is contained in certain columns
# #select all rows, and just the 'type' column with loc function
# games.loc[:,'type'] = pd.Categorical(games.loc[:,'type'])
#
# print(games.head()) #print first 5 rows
