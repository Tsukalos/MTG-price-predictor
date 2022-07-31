from numpy import sort
from scrapper.scryfall import Scryfall
import pandas as pd

keywords = sort(Scryfall.get_all_keywords())
idx = range(1,len(keywords)+1)
df = pd.DataFrame(keywords, index=idx, columns=['keyword'])
df.index.name = 'id'
df.to_csv('keywords.csv', sep=',')
