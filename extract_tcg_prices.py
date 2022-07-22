import scrapper
import time
import pandas as pd
import tqdm

tcg = scrapper.TCGpricing()

df = pd.read_csv('cards_1995_2003.csv')
df = df[pd.notnull(df['tcgplayer_id'])]
market_history = []
for id in tqdm.tqdm(df['tcgplayer_id']):
    time.sleep(0.2)
    market_history.append(tcg.get_history_pricing(id))

df['market_history'] = market_history
df.to_csv('cards_1995_2003.csv', sep=',', index=False)
# 17-07-2022
