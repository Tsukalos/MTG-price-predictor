import scrapper
import pandas as pd


fields_to_extract = [
    'name', 'tcgplayer_id',
    'cmc', 'keywords', 'layout', 'oversized', 'booster',
    'border_color', 'finishes', 'full_art',
    'promo', 'rarity', 'story_spotlight'
]
data = scrapper.Scryfall.get_all_pages('date>2003-07-28 date<2021-07-16 in:paper (f:standard or f:pioneer or f:modern' +
                              'or f:legacy or f:vintage or f:commander or f:explorer or f:brawl) (not:reprint or is:reprint)')

cards = []
for d in data:
    cards.append([d.get(k) for k in fields_to_extract])

cards = pd.DataFrame(cards, columns=fields_to_extract)
cards.to_csv('cards.csv', sep=',', index=False)
