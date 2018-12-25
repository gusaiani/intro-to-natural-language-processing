import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"Peach emoji is where it has always been. Peach is the superior "
          u"emoji. It's outranking eggplant 🍑 ")
print(doc[0].text)
print(doc[1].text)
print(doc[-1].text)
print(doc[17:19].text)

noun_chunks = list(doc.noun_chunks)
print(noun_chunks[0].text)

sentences = list(doc.sents)
assert len(sentences) == 3
print(sentences[1].text)
