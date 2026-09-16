from bs4 import BeautifulSoup
import csv

# append data to csv
def parse_html(html):
    fighters = []

    # init fighter id
    fighter_id = 0

    # convert each page to a list of stats
    for page in html:
        # create html soup object
        soup = BeautifulSoup(page, 'html.parser')
        rows = soup.select('tr')

        for row in rows:
            # reset temp arr each iteration
            fighter = []

            # get array of entries from row
            stats = row.select('td')

            if len(stats) <= 1:
                continue

            # append primary fighter key
            fighter.append(fighter_id)
            fighter_id += 1

            # isolate text from tags
            for i, stat in enumerate(stats):
                stats[i] = stat.text.strip()

            # combine first and last names
            fighter.append(stats[0] + ' ' + stats[1])
            
            # append without belt column
            for stat in stats[2:len(stats)-1]:
                fighter.append(stat)

            fighters.append(fighter)

                

    # open csv file
    with open("fighters.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # write to csv file
        for fighter in fighters:
            writer.writerow(fighter)

            