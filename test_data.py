import requests

url = "http://ufcstats.com/statistics/events/completed?page=all"

r = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')

# get name of event

rows = soup.select('tbody tr')

row = rows[1]

name = row.select_one('.b-link').text.strip()

print(name)

# get date of event

date = row.select_one('.b-statistics__date').text.strip()

print(date)

# get location of event

location = row.select_one('.b-statistics__table-col_style_big-top-padding').text.strip()

print(location)

# get link to the event

link = row.select_one('.b-statistics__table-content a')['href']

print(link)

# def open_html(path):
#     with open(path, 'rb') as f:
#         return f.read()