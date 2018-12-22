import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I love coffee')

print(doc.vocab.strings[u'coffee'])
print(doc.vocab.strings[3197928453018144401])
