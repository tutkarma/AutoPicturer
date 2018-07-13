from libkeywords import extract, search_tags


if __name__ == '__main__':
    text = ''
    with open("../parseRSS/articles/test19", encoding="utf-8") as f:
        text = f.read()
    tags = extract(text)
    #tags = ["lol", "kek", "azaz", "heh", "swsrgwsgr"]
    search_tags(tags)