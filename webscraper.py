import requests
from bs4 import BeautifulSoup
bachelors = []                                                                      # Declare Variable
bachelors_imgs = []                                                                 

show_website = requests.get('https://abc.com/shows/the-bachelorette/cast')          # Make a request to the site / get it as a string

soup = BeautifulSoup(show_website.content, 'html.parser')                           # Pass the string to a BeatifulSoup object
cast = soup.find_all(class_='tile__name')
cast_imgs = soup.find_all('picture')

the_bachelorette = cast[0].get_text()                                               # The Bachelorette data
the_bachelorette_img = cast_imgs[1]

chris_harrison_host = cast[1].get_text()                                            # Chris Harrison Data
chris_harrison_host_img = cast_imgs[1]

for i in range(2, len(cast, cast_imgs)):                                                       # Create list of the bachelors
    bachelors.append(cast[i].get_text())
    bachelors_imgs.append(cast_imgs[i])
