from client import FeedlyClient
from readability import Document
import requests
import re
import config

FEEDLY_REDIRECT_URI = "http://fabreadly.com/auth_callback"
FEEDLY_CLIENT_ID=config.USER_CONFIG['client_id']
FEEDLY_CLIENT_SECRET=config.USER_CONFIG['client_secret']
FEEDLY_STREAM=config.USER_CONFIG['category']

def clean_tags(html):
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', html)
    return clean_text


if __name__ == '__main__':
    feedly_client = FeedlyClient(token=FEEDLY_CLIENT_SECRET, sandbox=False)
    content = feedly_client.get_feed_content(FEEDLY_CLIENT_SECRET,FEEDLY_STREAM,unreadOnly=True)
    links = []
    for item in content['items']:
        links.append(item['originId'])

    for i, link in enumerate(links):
        html = requests.get(link).text
        doc = Document(html)
        text = doc.summary()
        text = clean_tags(text)
        with open(r'./articles/test{0:02d}'.format(i), 'w', encoding='utf8') as f:
            text = " ".join(text.split())
            f.write(text)