import spacy

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u'my fries were super gross')
doc2 = nlp(u'such disgusting flies')

similarity = doc1.similarity(doc2)
print(doc1.text, doc2.text, similarity)
