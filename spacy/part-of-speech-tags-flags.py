import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
apple = doc[0]
print('Fine-grained POS tag', apple.pos_, apple.pos)
print('Coarse-grained POS tag', apple.tag_, apple.tag)
print('Word shape', apple.shape_, apple.shape)
print('Alphanumeric characters?', apple.is_alpha)
print('Punctuation mark?', apple.is_punct)

print('')

billion = doc[10]
print('Digit?', billion.is_digit)
print('Like a number?', billion.like_num)
print('Like an email address?', billion.like_email)
