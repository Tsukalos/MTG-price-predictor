import scrython
import time
import tqdm


class Scryfall:

    @staticmethod
    def get_all_pages(query):
        page_count = 1
        page = scrython.cards.Search(q=query, page=page_count)
        all_data = []
        pbar = tqdm.tqdm(total=page.total_cards())
        while True:
            time.sleep(0.333)
            page = scrython.cards.Search(q=query, page=page_count)
            page_data = page.data()
            all_data = all_data + page_data
            pbar.set_description("Processing page {}".format(page_count))
            pbar.update(len(page_data))
            page_count += 1
            if not page.has_more():
                break
        pbar.close()
        return all_data
