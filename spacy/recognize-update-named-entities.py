import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'San Francisco considers banning sidewalk delivery robots')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

from spacy.tokens import Span

doc = nlp(u'FB is hiring a new VP of global policy')
doc.ents = [Span(doc, 0, 1, label=doc.vocab.strings[u'ORG'])]
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
