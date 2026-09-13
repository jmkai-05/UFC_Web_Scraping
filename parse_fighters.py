from bs4 import BeautifulSoup
import csv

# append data to csv
def parse_html(html):
    fighters = []

    # convert each page to a list of stats
    for page in html:
        # create html soup object
        soup = BeautifulSoup(page, 'html.parser')
        rows = soup.select('tr')

        for row in rows:
            # get array of entries from row
            stats = row.select('td')

            if len(stats) <= 1:
                continue

            # isolate text from tags
            for i, stat in enumerate(stats):
                stats[i] = stat.text.strip()
                # print(stat.text.strip())
            
            # append without belt column
            fighters.append(stats[0:len(stats)-1])

    # open csv file
    with open("fighters.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # write to csv file
        fighter_id = 0
        for fighter in fighters:
            fighter.insert(0, fighter_id)
            writer.writerow(fighter)

            fighter_id += 1
            