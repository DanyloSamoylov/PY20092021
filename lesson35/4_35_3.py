"""
Requests using multiprocessing

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
"""
import requests
import json
import threading
from pprint import pprint


def request_url(url_, params_, text_, lock_):

    resp = requests.get(url_+f'?q={text_}', params=params_)
    lock_.acquire()
    data = resp.json()['data']
    comment = {text_: [com.get('body') for com in data]}

    # pprint(comment)

    try:
        with open('comment_text.json', 'r') as file:
            data_ = json.load(file)
            pprint(data_)
    except:
        data_ = dict()

    data_.update(comment)
    with open('comment_text.json', 'w') as file:
        json.dump(data_, file, indent=4)
    lock_.release()


url_addr = 'https://api.pushshift.io/reddit/search/comment'
text_request = ['idleheroes', 'Aspen', 'Fiona']
params = {
    'subreddit': 'games',
    'size': 100,
    'sort_type': 'created_utc'
}
lock = threading.Lock()
threads = []
for text in text_request:
    thread = threading.Thread(target=request_url, args=(url_addr, params, text, lock))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
