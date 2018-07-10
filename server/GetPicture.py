from flickrapi import FlickrAPI
from pprint import pprint

FLICKR_PUBLIC = '34aa2081ba0205515b1eb902b3cc6809'
FLICKR_SECRET = '287c0a744b071037'

def FromURL(tags):
    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_o'
    text = " ".join(tags)
    request = flickr.photos.search(text=text, per_page=1, extras=extras)
    print(request['photos'])
    return request['photos']['photo'][0]['url_o']
