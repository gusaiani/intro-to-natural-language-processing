import spacy
nlp = spacy.load('en_core_web_sm')

text = open('customer_feedback_627.txt', 'r').read()
doc = nlp(text)
doc.to_disk('customer_feedback_627.bin')
