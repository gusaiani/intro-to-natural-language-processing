import spacy

from spacy.tokens import Doc
from spacy.vocab import Vocab

doc = Doc(Vocab()).from_disk('customer_feedback_627.bin')

print(doc)
