import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Give it back! He pleaded.')

print(doc[0].text)
print(doc[1])
span = doc[1:4]
print(span.text)
