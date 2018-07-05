from client import FeedlyClient
from readability import Document
import requests
import config

FEEDLY_REDIRECT_URI = "http://fabreadly.com/auth_callback"
FEEDLY_CLIENT_ID=config.USER_CONFIG['client_id']
FEEDLY_CLIENT_SECRET=config.USER_CONFIG['client_secret']
FEEDLY_STREAM=config.USER_CONFIG['category']

feedly_client = FeedlyClient(token=FEEDLY_CLIENT_SECRET, sandbox=False)
content = feedly_client.get_feed_content(FEEDLY_CLIENT_SECRET,FEEDLY_STREAM,unreadOnly=True)
links = []
for item in content['items']:
    links.append(item['originId'])
link = links.pop()
html = requests.get(link).text
doc = Document(html)
s = doc.summary()
print(s)