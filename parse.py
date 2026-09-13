from bs4 import BeautifulSoup
import csv

def parse_html(html):
    # create html soup object
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('tr')

    # open csv file
    with open("fighters.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for row in rows:
            # get array of entries from row
            stats = row.select('td')

            # isolate text from tags
            for i, stat in enumerate(stats):
                stats[i] = stat.text.strip()
                # print(stat.text.strip())
            
            # write to csv file
            writer.writerow(stats)
            