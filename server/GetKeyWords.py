from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, sent_tokenize, pos_tag_sents
from itertools import takewhile, tee, chain
import networkx as nx
import re
import sys

def textrank(words, candidates, n_keywords=0.05):
    graph = nx.Graph()
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
    ranks = nx.pagerank(graph)
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

def extract_candidate_words(text, good_tags):
    text = re.sub(r'[^\w\s]','',text)
    stops = set(stopwords.words('english'))
    wnl = WordNetLemmatizer()
    tagged_words = chain.from_iterable(pos_tag_sents(word_tokenize(sent) for sent in sent_tokenize(text)))
    candidates = [wnl.lemmatize(word) for word, tag in tagged_words if tag in good_tags and word not in stops]
    return candidates

def Extract(text):

    words = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]
    good_tags = set(['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'NNPS'])
    candidates = extract_candidate_words(text, good_tags)
    res = textrank(words, candidates)
    result = []
    for (cnt, word) in zip(range(5), res):
        result.append(word[0])
    return result

