import yake
from urllib.request import urlopen
kw_extractor = yake.KeywordExtractor()


def rec(text, max_ngram_size=2, deduplication_threshold=0.5, numOfKeywords=15):
    language = "en"
    custom_kw_extractor = yake.KeywordExtractor(
        lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    links = []
    url = 'https://en.wikipedia.org/wiki/'
    for kw in keywords:
        new_url = url + str(kw[0])
        try:
            if(urlopen(new_url)):
                links.append(new_url)
            print(links)
        except:
            print("invalid")
    return links
