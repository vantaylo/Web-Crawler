import requests
import pymongo

from bs4 import BeautifulSoup
from pymongo import MongoClient

def main():
    cast_members = dict()
    cast_member_name = str()
    
    ## Get Data
    show_website = requests.get('https://abc.com/shows/the-bachelorette/cast')          # Make a request to the site / get it as a string

    soup = BeautifulSoup(show_website.content, 'html.parser')                           # Pass the string to a BeatifulSoup object
    cast = soup.find_all(class_='tile__name')
    cast_imgs = soup.find_all('picture')
    cast_details = soup.find_all(class_='tile__desc')

    cast_members = {}
    # print(cast_details)

    for i in range(len(cast)):                                                          # TV show cast data
        cast_member_name = cast[i].get_text().replace(".", "")
        cast_member_img = cast_imgs[i]
        cast_member_info = cast_details[i].get_text()
        # print("*", cast_member_name, ":", cast_member_info)                           # Debug

        cast_members[cast_member_name] = cast_member_info
        

    # Store Data
    client = pymongo.MongoClient("mongodb+srv://vantaylo:bach2020@cluster0.mxv1u.mongodb.net/test?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)   # Access client
    
    db = client.the_bachelorette_2020                            # Access databases
    
    collection = db.cast_members                                 # Access collection

    collection.insert_one(cast_members)                          # Send show data to db
  
main()