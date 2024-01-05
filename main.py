import spacy
from transformers import *
from tools import text, get_entities_html

ner = pipeline("ner", model="dslim/bert-base-NER")
ner2 = pipeline("ner", model="xlm-roberta-large-finetuned-conll03-english")
ner3 = pipeline("ner", model="Jean-Baptiste/roberta-large-ner-english")

doc_ner = ner(text)
doc_ner2 = ner2(text)
doc_ner3 = ner3(text)

get_entities_html(text, doc_ner)
get_entities_html(text, doc_ner2)
get_entities_html(text, doc_ner3)
