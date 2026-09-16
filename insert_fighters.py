# activate venv
import parse_fighters
import time
import random
import utl

def main():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

    html_arr = []

    # iterate through alphabet
    for char in alpha:
        # collect page html
        html = utl.get_html(f"http://ufcstats.com/statistics/fighters?char={char}&page=all")
        
        # save html in an array
        html_arr.append(html)

        # rate limiter
        time.sleep(random.uniform(1, 3))

    # Push array of html pages to csv
    parse_fighters.parse_html(html_arr)


if __name__ == '__main__':
    main()

