from flask import Flask
from libkeywords import extract, search_tags

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    file_name = input()

    with open(file_name, 'r', encoding='utf8') as f:
        text = f.read()

    tags = extract(text)
    url = search_tags(tags)
    print(url)