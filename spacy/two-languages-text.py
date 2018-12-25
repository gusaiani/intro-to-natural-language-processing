import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Hello, world. Here are two sentences.')
print([t.text for t in doc])

nlp_de = spacy.load('de_core_news_sm')
doc_de = nlp(u'Ich bin ein Berliner.')
print([t.text for t in doc_de])
