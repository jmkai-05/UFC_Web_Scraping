import creds
import pymysql
import requests
from bs4 import BeautifulSoup

def convert_height(height):
    feet = int(height[0])

    if(height[3] == '"'):
        inch = int(height[2])
    else:
        inch = 10 + int(height[3])
    
    return feet * 30.48 + inch * 2.54

def convert_weight(weight):
    return 100 * int(weight[0]) + 10 * int(weight[1]) + int(weight[2])

url = "http://ufcstats.com/statistics/fighters?char=a&page=all"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.select('tbody tr')

row = rows[1]

names = row.select('.b-link')

stats = row.select('td')

first_name = stats[0].text.strip()

print(first_name)

last_name = stats[1].text.strip()

print(last_name)

nickname = stats[2].text.strip()

if(nickname != ''):
    print(nickname)
else:
    print('--')

# print(stats)

height = stats[3].text.strip()
if(height != "--"):
    height = convert_height(height)

print(height)

weight = stats[4].text.strip()
if(weight != "--"):
    weight = convert_weight(weight)

print(weight)

reach = stats[5].text.strip()

print(reach)

stance = stats[6].text.strip()

if(stance != ''):
    print(stance)
else:
    print('--')

wins = int(stats[7].text.strip())

print(wins)

losses = int(stats[8].text.strip())

print(losses)

draws = int(stats[9].text.strip())

print(draws)

# conn = pymysql.connect(
#     host='172.26.176.1',
#     port=3306,
#     user=creds.USERNAME,
#     password=creds.PASSWORD,
#     database='mydb'
# )

# cursor = conn.cursor()

# cursor.execute(
#     "INSERT INTO fighters VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
#     (first_name, "Hooker", "Switch", 24, 13)
# )

# conn.commit()