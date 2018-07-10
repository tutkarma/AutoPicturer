from flask import Flask

import GetKeyWords
import GetPicture

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    fileName = input()

    with open(fileName, 'r', encoding='utf8') as f:
        text = f.read().lower()

    tags = GetKeyWords.Extract(text)
    print(tags)
    url = GetPicture.FromURL([tags[0], tags[1]])
    print(url)