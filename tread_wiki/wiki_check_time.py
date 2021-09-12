import time
import requests


def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

print("Running without threads:")
without_threads_start = time.time()
for url in wiki_page_urls:
    print(get_wiki_page_existence(wiki_page_url=url))
print("Without threads time:", time.time() - without_threads_start)
