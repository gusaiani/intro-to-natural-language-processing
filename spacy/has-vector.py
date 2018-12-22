import spacy

nlp = spacy.load('en_core_web_lg')
tokens = nlp(u'dog cat banana perfunctory afskfsd')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
