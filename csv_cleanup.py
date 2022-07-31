
from ast import literal_eval
import pandas as pd
import numpy as np

c = literal_eval
df = pd.read_csv('cardss.csv', sep=',', converters={
                 'market_history': c, 'keywords': c, 'finishes': c})

### fixing id column
df['tcgplayer_id'] = df['tcgplayer_id'].astype(int)

### cleans empty price history lists
df = df[df['market_history'].apply(len).gt(0)]

### orders normal variants to first position
for i in df['market_history']:
    if len(i) > 1 and i[0][0] == 'Foil':
        temp = i[0]
        i[0] = i[1]
        i[1] = temp

reindex_df = df.reset_index()
reindex_df

# borders = df['border_color'].unique()
# layouts = df['layout'].unique()
# rarities = df['rarity'].unique()


### generate dummys enconding

keywords_df = pd.DataFrame(df['keywords'].tolist())
keywords_obj = keywords_df.stack(dropna=False)
keywords_df = pd.get_dummies(keywords_obj)
keywords_df = keywords_df.sum(level=0)

### create new df

new_df = pd.concat([reindex_df, keywords_df], axis=1)
new_df


new_df.to_csv('cards_.csv', sep=',', index=False)
