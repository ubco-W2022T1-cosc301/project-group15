# Edwin

import pandas as pd
import re

def dataloadnclean(path):
    dataset = pd.read_csv(path)
    dataset = (
        dataset
        [dataset['types'] != 'bundle']
        .drop(columns = ['url', 'game_description', 'minimum_requirements', 'recommended_requirements', 'desc_snippet', 'mature_content', 'types', 'discount_price'])
        [dataset['all_reviews'].notna() & dataset['all_reviews'].str.contains('%')]
        .assign(all_reviews = lambda x: x['all_reviews'].apply(lambda y: int(re.findall("(\d{1,3}%)", y)[0].replace('%', ''))))
        [dataset['recent_reviews'].notna() & dataset['recent_reviews'].str.contains('%')]
        .assign(recent_reviews = lambda x: x['recent_reviews'].apply(lambda y: int(re.findall("(\d{1,3}%)", y)[0].replace('%', ''))))
        [dataset['original_price'].notna() & (dataset['original_price'].str.contains('\$') | dataset['original_price'].str.contains('free', case=False))]
        .assign(original_price = lambda x: x['original_price'].apply(lambda y: 0 if 'free' in y.lower() else float(y.replace('$', ''))))
    )
    return dataset