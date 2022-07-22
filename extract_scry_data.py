import scrapper
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('query', type=str,
                    help='Query string to search on Scryfall API.')
parser.add_argument('-f', '--filename', type=str,
                    help='File to store the query results', default='cards.csv')
parser.add_argument('-cf', '--card_fields', nargs='+',
                    help='Fields to extract from each card object obtained from the query')

args = parser.parse_args()

if (args.card_fields):
    fields_to_extract = args.card_fields
else:
    fields_to_extract = [
        'name', 'tcgplayer_id',
        'cmc', 'keywords', 'layout', 'oversized', 'booster',
        'border_color', 'finishes', 'full_art',
        'promo', 'rarity', 'story_spotlight'
    ]

query = args.query
filename = args.filename

data = scrapper.Scryfall.get_all_pages(query)

cards = []
for d in data:
    cards.append([d.get(k) for k in fields_to_extract])

cards = pd.DataFrame(cards, columns=fields_to_extract)
cards.to_csv(filename, sep=',', index=False)
