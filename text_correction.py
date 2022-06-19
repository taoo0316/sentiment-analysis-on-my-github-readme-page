# Import textblob
from textblob import TextBlob

# Using textblob's correct() function
text = 'He is a gret peron. He beleves in fod.'
text=TextBlob(text)
print(text.correct())