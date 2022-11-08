# Adrian
import pandas as pd
import numpy as np
import re

def dataFilter(path): 
    game = pd.read_csv(path)
    dset = (
        game[
        game['types'] != 'bundle']
        .drop(columns= ["url", "types", "desc_snippet","achievements","game_description","mature_content","minimum_requirements","recommended_requirements","discount_price"], inplace=False)
        .drop_duplicates(subset="name", keep='first', inplace=False, ignore_index=False)
        .rename(columns={"name": "Game Name", "recent_reviews": "Recent Review", "all_review": "All Review", "release_date": "Release Date", "developer": "Developer","publisher": "Publisher", "popular_tags": "Game Tags", "game_details": "Game Details", "languages": "Languages", "genre": "Genre", "original_price": "Price"})
        .loc[game["name"].notnull()]
        .loc[game["recent_reviews"].notnull()]
        .loc[game["all_reviews"].notnull()]
        .loc[game["release_date"].notnull()]
        .loc[game["developer"].notnull()]
        .loc[game["publisher"].notnull()]
        .loc[game["popular_tags"].notnull()]
        .loc[game["languages"].notnull()]
        .loc[game["genre"].notnull()]
        .loc[game["original_price"].notnull()]
    )
    return dset

def dataFilter2(path):
    game = (
        pd.read_csv(path)
    )
    df = (
        game
        [game['types'] != 'bundle']
        .drop(columns= ["url","types", "desc_snippet","achievements","game_description","mature_content","minimum_requirements","recommended_requirements","discount_price"], inplace=False)
        .drop_duplicates(subset="name", keep='first', inplace=False, ignore_index=False)
        .rename(columns={"name": "Game Name", "recent_reviews": "Recent Review", "all_review": "All Review", "release_date": "Release Date", "developer": "Developer","publisher": "Publisher", "popular_tags": "Game Tags", "game_details": "Game Details", "languages": "Languages", "genre": "Genre", "original_price": "Price"})
        # .loc[game["name"].notnull()]
        # .loc[game["recent_reviews"].notnull()]
        # .loc[game["all_reviews"].notnull()]
        .loc[game["release_date"].notnull()]
        .loc[game["developer"].notnull()]
        .loc[game["publisher"].notnull()]
        # .loc[game["popular_tags"].notnull()]
        # .loc[game["languages"].notnull()]
        # .loc[game["genre"].notnull()]
        .loc[game["original_price"].notnull()]   
    )
    return df

def split_value2(list, column_name, index):
    if (re.search(',', list[column_name][index])):
        first_half  = list[column_name][index][:len(list[column_name][index])//2]
        return first_half
    elif(list[column_name][index][:len(list[column_name][index])//2] == list['Developer'][index]):
        return list['Developer'][index]
    else:
        return list[column_name][index]
    
def split_value1(list, column_name):
    count = 0
    temp = []
    for x in list[column_name]:
        if(x != '' and x != 39093909 and x != '(none),(none)'):
            try:
                split = split_value2(list, column_name, count)
                # print(split)
                list[column_name] = list[column_name].replace(list[column_name][count], split)
                # print(list[column_name][count])
            except:
                # print('Row: ', count, ' Value ', x, 'error')
                pass
        count+= 1
    return list