import pandas as pd
import numpy as np

def dataloadnclean(path):
    dataset = pd.read_csv(path)
    dataset = (
        dataset
        .sort_values("user_review", ascending = False)
        .drop(index = dataset[dataset["user_review"] == "tbd"].index)
        .drop_duplicates(subset = ["name"])
        #.drop(columns = 'platform')
    )
    return dataset