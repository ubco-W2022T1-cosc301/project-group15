# Adrian
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

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

def split_value(list, column_name, name, game_name):
    count = 0
    index = -1
    for i in list[name]:
        if (i == game_name):
            index = count
        count+= 1
    
    if(column_name == 'languages'):
        return re.split('[\b\W\b]+',list[column_name][index])
    elif(index != -1):
        return re.split('[;,.]\s*',list[column_name][index])
    else:
        return []
    
def unique_game_tags(list, column_name, name):
    count = 0
    index = -1
    unique = []
    for x in list[name]:
        temp = []
        for i in list[name]:
            if (i == x):
                index = count
                break
            count+= 1
        try:    
            if(column_name == 'languages'):
                temp = re.split('[\b\W\b]+',list[column_name][index])
            elif(index != -1):
                temp = re.split('[;,.]\s*',list[column_name][index])
            else:
                temp = []
                
            for y in temp:
                confirm = 0
                for z in unique:
                    if(y == z):
                        confirm+=1
                        break
                
                if(confirm == 0):
                    unique.append(y)
        except:
            pass
                
    return unique     

def unique_game_tags2(list, column_name, name):
    count = 0
    index = -1
    unique = []
    dict = {}
    for x in list[name]:
        temp = []
        for i in list[name]:
            if (i == x):
                index = count
                break
            count+= 1
        try:    
            if(column_name == 'Languages'):
                temp = re.split('[\b\W\b]+',list[column_name][index])
            elif(index != -1):
                temp = re.split('[;,.]\s*',list[column_name][index])
            else:
                temp = []
                
            for y in temp:
                confirm = 0
                for z in unique:
                    if(y == z):
                        confirm+=1
                        dict[y] += 1
                        break
                
                if(confirm == 0):
                    unique.append(y)
                    dict[y] = 1
        except:
            pass
                
    return dict      

def addlabel2(x,y):
    for i in range(len(x)):
        plt.text(y[i],x[i],y[i]) 