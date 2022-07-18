import requests
from requests.exceptions import HTTPError
import json


class TCGPhistory(object):
    def __init__(self):
        self.baseurl = "https://infinite-api.tcgplayer.com/price/history/"
        self.headers = {"Accept": "application/json"}

    def get_history_pricing(self, id, frame='annual', offset=2):
        url = self.baseurl + '{0}?range={1}'.format(id, frame)
        response = requests.get(url, self.headers)
        if not response:
            raise HTTPError(response.status_code)
        parsed = json.loads(response.text)
        parsed = parsed['result'][offset:][::-1]
        history = []
        history_count = len(parsed)
        n_variants = len(parsed[offset]['variants'])

        # getting names of variants and setting the lists to hold the history
        for i in range(n_variants):
            history.append((parsed[0]['variants'][i]['variant'], []))

        for i in range(n_variants):
            for j in range(history_count):
                history[i][1].append(parsed[j]['variants'][i]['marketPrice'])
        return history
