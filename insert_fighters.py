# activate venv
from playwright.sync_api import sync_playwright
import parse
import time

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']

with sync_playwright() as p:
    # Launch a headless browser browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # iterate through alphabet
    for char in alpha:
        # Navigate to the page (Playwright will wait and process the challenge)
        page.goto(f"http://ufcstats.com/statistics/fighters?char={char}&page=all")
        
        # Wait for a specific element that exists only on the actual site
        page.wait_for_selector("tr", timeout=10000)
        
        # Extract the resolved HTML
        html = page.content()

        parse.parse_html(html)

        time.sleep(5)
    
    browser.close()

'''
for letter in alphabet:
    url = f"http://ufcstats.com/statistics/fighters?char={letter}&page=all"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    rows = soup.select('title')

    print(rows[0].text)
    
# first_name = text_funcs.get_first_name(stats[0])
# last_name = text_funcs.get_last_name(stats[1])
# nickname = text_funcs.get_nickname(stats[2])
# height = text_funcs.get_height(stats[3])
# weight = text_funcs.get_weight(stats[4])
# reach = text_funcs.get_reach(stats[5])
# stance = text_funcs.get_stance(stats[6])
# wins = text_funcs.get_wins(stats[7])
# losses = text_funcs.get_losses(stats[8])
# draws = text_funcs.get_draws(stats[9])

'''