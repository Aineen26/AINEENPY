
import time

import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
current_page = "/"

while current_page:
    try:
        response = requests.get(base_url + current_page, timeout=10)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        if not quotes:
            print("Warning: No quotes found on this page.")

        for q in quotes:
            try:
                text = q.find('span', class_='text').text
                author = q.find('small', class_='author').text
                print(f"“{text}” — {author}")
            except AttributeError:
                print("Skipping a quote due to missing data tags.")

        next_button = soup.find('li', class_='next')
        if next_button:
            current_page = next_button.find('a')['href']
            print(f"\n--- Moving to: {current_page} ---\n")
            time.sleep(1)  
        else:
            current_page = None

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
        break
    except requests.exceptions.ConnectionError:
        print("Error: DNS failure or refused connection. Check your internet.")
        break
    except requests.exceptions.Timeout:
        print("Error: The request timed out. The server might be slow.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break

print("Scraping finished.")
