text="I am a computer science student a Yale-NUS College, the leading liberal arts college in Asia. There, I was able to take classes across disciplines and academic traditions, which helped me become a more methodical thinker, learner and communicator."
# Coverting the text into a spacy Doc

import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp(text)

# Using spacy's pos_ attribute to check for part of speech tags
for token in doc:
  if token.pos_=='NOUN' or token.pos_=='PROPN':
    print(token.text)