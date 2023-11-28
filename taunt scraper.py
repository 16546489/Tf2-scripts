import requests
from bs4 import BeautifulSoup
import re

def get_taunt_names(url, css_selector):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table containing the taunt information using the specified CSS selector
        taunt_table = soup.select_one(css_selector)

        if taunt_table:
            # Extract names using regular expressions
            taunt_names = [re.sub(r'\s*\(.+?\)\s*', '', cell.text.strip()) for row in taunt_table.find_all('tr')[1:] for cell in row.find_all('td')]

            # Filter out names without alphabetic characters
            taunt_names = [name for name in taunt_names if any(char.isalpha() for char in name)]

            # Print each taunt name on a separate row
            for taunt_name in taunt_names:
                print(taunt_name)
        else:
            print(f"Error: Taunt table not found using the CSS selector: {css_selector}")

    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")

if __name__ == "__main__":
    # URL of the page containing taunt information
    url = "https://wiki.teamfortress.com/wiki/Template:Storepurchasable"

    # CSS selector for the taunts table
    css_selector = "#mw-content-text > div > table:nth-child(16)"

    # Get and print the list of taunt names from the page using the specified CSS selector
    get_taunt_names(url, css_selector)
