import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_lg')

doc_dep = nlp(u'This is a sentence.')

displacy.serve(doc_dep, style='dep')

doc_ent = nlp(u'When Sebastian Thrun started working on self-driving cars at Google '
              u'in 2007, few people outside of the company took him seriously.')

displacy.serve(doc_ent, style='ent')
