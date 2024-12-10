import requests
import time

url_1 = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
response = requests.get(url_1)
top_data_ids = response.json()

top30_data = top_data_ids[:30]

data_lists = []

for data_id in top30_data:
    url_2 = f"https://hacker-news.firebaseio.com/v0/item/{data_id}.json?print=pretty"
    response_2 = requests.get(url_2)
    dic_data = response_2.json()

    if dic_data and "url" in dic_data:
        data_lists.append({"title": dic_data.get("title", "No title"), "link": dic_data.get("url", None)})
    else:
        continue

    time.sleep(1)

for data in data_lists:
    print(data)
