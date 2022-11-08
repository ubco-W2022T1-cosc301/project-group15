# Adrian
import pandas as pd
import numpy as np

def dataFilter(path2): 
    game = (
        pd.read_csv(path2)
    )
    df = (
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
    return df