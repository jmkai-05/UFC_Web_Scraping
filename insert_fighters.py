from bs4 import BeautifulSoup
import text_funcs
import time
import pymysql
import creds
import requests

ASCII_OFFSET = 26

# connect to local sql server
conn = pymysql.connect(
    host='172.26.176.1',
    port=3306,
    user=creds.USERNAME,
    password=creds.PASSWORD,
    database='mydb'
)

cursor = conn.cursor()

fighter_id = 0

for j in range(1, 27):
    url = f"http://ufcstats.com/statistics/fighters?char={chr(j + ASCII_OFFSET)}&page=all"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        stats = row.select('td')

        if(len(stats) != 11): continue

        first_name = text_funcs.get_first_name(stats[0])
        last_name = text_funcs.get_last_name(stats[1])
        nickname = text_funcs.get_nickname(stats[2])
        height = text_funcs.get_height(stats[3])
        weight = text_funcs.get_weight(stats[4])
        reach = text_funcs.get_reach(stats[5])
        stance = text_funcs.get_stance(stats[6])
        wins = text_funcs.get_wins(stats[7])
        losses = text_funcs.get_losses(stats[8])
        draws = text_funcs.get_draws(stats[9])

        cursor.execute(
            "INSERT INTO fighters VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (fighter_id, first_name, last_name, nickname, height, weight, reach, stance, wins, losses, draws)
        )

        fighter_id += 1

    # prevent overrequesting
    time.sleep(1)

conn.commit()
