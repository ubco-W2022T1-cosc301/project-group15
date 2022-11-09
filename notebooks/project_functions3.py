# Sitt

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def dataloadnclean(path):
    gamedataset = pd.read_csv(path)
    gamedata=(
        gamedataset
        .drop(columns=["url", "types", "game_description", "achievements", "minimum_requirements", "mature_content","recommended_requirements", "discount_price"])
        .drop_duplicates(subset=["name"], inplace=False)
)
    return gamedata

