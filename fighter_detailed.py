from bs4 import BeautifulSoup
import requests

url = "http://ufcstats.com/statistics/fighters?char=a&page=all"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.select('tbody tr')

row = rows[1]

stats = row.select_one('a')

link = stats['href']

print(link)
