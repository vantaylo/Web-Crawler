import requests
import pymongo

from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

database_password = os.getenv("DB_PASSWORD")                                     # Environment variables
twitter_apiKey = os.getenv("TWITTER_API_KEY")                       
twitter_apiKey_secret = os.getenv("TWITTER_API_KEY_SECRET")
twitter_bearerToken = os.getenv("TWITTER_BEARER_TOKEN")
twitter_accessToken = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_accessToken_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def main():
    print("**", database_password)

    cast_members = dict()
    cast_member_name = str()
    
    ## Get Show Data
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
        

    ## Store Show Data
    client = pymongo.MongoClient(f"mongodb+srv://vantaylo:{database_password}@cluster0.mxv1u.mongodb.net/test?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)   # Access client
    
    db = client.the_bachelorette_2020                               # Access databases
    
    collection = db.cast_members                                    # Access collection

    collection.insert_one(cast_members)                             # Send show data to db


main()