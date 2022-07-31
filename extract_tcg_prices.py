import scrapper
import time
import pandas as pd
import tqdm

tcg = scrapper.TCGpricing()

df = pd.read_csv('cards_.csv')
df = df[pd.notnull(df['tcgplayer_id'])]
market_history = []
pbar = tqdm.tqdm(df['tcgplayer_id'])
for id in pbar:
    time.sleep(0.1)
    pbar.set_description("Processing card id={}".format(int(id)))
    market_history.append(tcg.get_history_pricing(int(id)))

df['market_history'] = market_history
df.to_csv('cards_.csv', sep=',', index=False)
# 17-07-2022
