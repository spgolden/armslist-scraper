#!/usr/bin/env python

import sys
import requests

from models.listing import Listing

def scrape_listing(url):
    response = requests.get(url)
    listing = Listing(response.content)
    print('Title: ' + listing.title)
    print('Price: ' + listing.price)
    print('Image URLs: ' + listing.imgs)
    print('Location: ' + listing.location)
    print('Description: ' + listing.description)
    print('Category: ' + listing.category)
    print('Manufacturer: ' + listing.manufacturer)
    print('Caliber: ' + listing.caliber)
    print('Action: ' + listing.action)
    print('Firearm Type: ' + listing.firearm_type)
    print('Listing Date: ' + listing.listed_date)
    print('Post ID: ' + listing.post_id)
    print('Registration: ' + str(listing.registered))
    print('Party Type: ' + listing.party)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('url required')
        sys.exit()

    url = str(sys.argv[1])
    scrape_listing(url=url)
