# Edwin

import pandas as pd
import re

def dataloadnclean(path):
    dataset = pd.read_csv(path)
    dataset = (
        dataset
        [dataset['types'] != 'bundle']
        .drop(columns = ['url', 'game_description', 'minimum_requirements', 'recommended_requirements', 'desc_snippet', 'mature_content', 'types'])
        [dataset['all_reviews'].notna() & dataset['all_reviews'].str.contains('%')]
        .assign(all_reviews = lambda x: x['all_reviews'].apply(lambda y: re.findall("(\d{1,3}%)", y)[0].replace('%', '').to_int()))
        [dataset['recent_reviews'].notna() & dataset['recent_reviews'].str.contains('%')]
        .assign(recent_reviews = lambda x: x['recent_reviews'].apply(lambda y: re.findall("(\d{1,3}%)", y)[0].replace('%', '').to_int()))
    )
    return dataset