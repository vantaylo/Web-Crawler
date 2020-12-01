from bs4 import BeautifulSoup
import requests

# Anchor extraction from HTML document

show_website = requests.get('https://www.nbc.com/the-voice/credits/artists/season-19')
soup = BeautifulSoup(show_website.content, 'html.parser')
artists = soup.findAll("div", {"class": "grid__tiles"})
print(artists)