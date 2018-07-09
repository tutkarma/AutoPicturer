from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, pos_tag_sents
from itertools import takewhile, tee
import networkx
import re
import sys

def textrank(words, candidates, n_keywords=0.05):
    graph = networkx.Graph()
    graph.add_nodes_from(set(candidates))
    def pairwise(iterable):
        """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
    for w1, w2 in pairwise(candidates):
        if w2:
            graph.add_edge(*sorted([w1, w2]))
    # score nodes using default pagerank algorithm, sort by score, keep top n_keywords
    ranks = networkx.pagerank(graph)
    if 0 < n_keywords < 1:
        n_keywords = int(round(len(candidates) * n_keywords))
    word_ranks = {word_rank[0]: word_rank[1] for word_rank in sorted(ranks.items(), key=lambda x: x[1], reverse=True)[:n_keywords]}
    keywords = set(word_ranks.keys())
    # merge keywords into keyphrases
    keyphrases = {}
    j = 0
    for i, word in enumerate(words):
        if i < j:
            continue
        if word in keywords:
            kp_words = list(takewhile(lambda x: x in keywords, words[i:i+10]))
            avg_pagerank = sum(word_ranks[w] for w in kp_words) / float(len(kp_words))
            keyphrases[' '.join(kp_words)] = avg_pagerank
            j = i + len(kp_words)
    return sorted(keyphrases.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    file_name = sys.argv[1]
    words = []
    with open(file_name, 'r', encoding='utf8') as f:
        text = f.read().lower()
    text = re.sub(r'[^\w\s]','',text)
    words = text.split()
    stops = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stops and len(word)>=4]
    wnl = WordNetLemmatizer()
    words = [wnl.lemmatize(i) for i in filtered_words]
    tagged_words = pos_tag(words)
    good_tags=set(['JJ','JJR','JJS','NN','NNP','NNS','NNPS'])
    candidates = [word for word, tag in tagged_words if tag in good_tags]
    res = textrank(words, candidates)
    for cnt, word in enumerate(res):
        if cnt > 4:
            break
        print(word[0])
