import spacy
import pytextrank
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")


def extract_summary(data, limit_sentences=5, preserve_order=True):
    summary = []
    text = str(data)
    doc = nlp(text)
    tr = doc._.textrank
    sum = ''
    for sent in tr.summary(limit_phrases=15, limit_sentences=limit_sentences, preserve_order=preserve_order):
        if(sum == ''):
            sum = str(sent)
            continue
        sum = sum + '. ' + str(sent)
    summary.append(sum)
    return summary
