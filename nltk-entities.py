import nltk # nltk-entities.py

sentence = "At seven PM on Friday evening the sky was blue"

tokens = nltk.word_tokenize(sentence)
print("tokens:",tokens)

tagged = nltk.pos_tag(tokens)
print("tagged:",tagged)

entities = nltk.chunk.ne_chunk(tagged)
print("entities:",entities)

