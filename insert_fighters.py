import time
import creds
import pymysql
import requests
from bs4 import BeautifulSoup

ASCII_OFFSET = 96

def convert_height(height):
    feet = int(height[0])

    if(height[3] == '"'):
        inch = int(height[2])
    else:
        inch = 10 + int(height[3])
    
    return feet * 30.48 + inch * 2.54

def convert_weight(weight):
    return 100 * int(weight[0]) + 10 * int(weight[1]) + int(weight[2])

with pymysql.connect(
    host='172.26.176.1',
    port=3306,
    user=creds.USERNAME,
    password=creds.PASSWORD,
    database='mydb'
) as conn:
    with conn.cursor() as cursor:
        conn.commit()

        fighter_id = 0

        for j in range(1, 27):

            url = f"http://ufcstats.com/statistics/fighters?char={chr(j + ASCII_OFFSET)}&page=all"

            r = requests.get(url)

            soup = BeautifulSoup(r.content, 'html.parser')

            rows = soup.select('tbody tr')

            for row in rows:

                stats = row.select('td')

                if(len(stats) < 4):
                    continue

                fighter_id += 1

                first_name = stats[0].text.strip()

                last_name = stats[1].text.strip()

                nickname = stats[2].text.strip()

                if(nickname == ''):
                    nickname = '--'

                height = stats[3].text.strip()

                if(height == "--"):
                    height = -1
                else:
                    height = convert_height(height)

                weight = stats[4].text.strip()
                
                if(weight == "--"):
                    weight = -1
                else:
                    weight = convert_weight(weight)

                reach = stats[5].text.strip()

                if(reach == '--'):
                    reach = -1
                else:
                    reach = float(reach[0:4])

                stance = stats[6].text.strip()

                if(stance == ''):
                    stance = '--'

                wins = int(stats[7].text.strip())

                losses = int(stats[8].text.strip())

                draws = int(stats[9].text.strip())

                cursor.execute(
                    "INSERT INTO fighters VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (fighter_id, first_name, last_name, nickname, height, weight, reach, stance, wins, losses, draws)
                )

                conn.commit()
            
            time.sleep(5)
