import spacy
import string
import json

punct = string.punctuation
nlp = spacy.load("xx_ent_wiki_sm")

def getlvstopwords():
    stopwords_file = open('stopwords-lv2.json', 'r', encoding="utf8")
    stopwords_arr = json.load(stopwords_file)
    return stopwords_arr

def datu_prieksapstrade(raksts):
  stopwords_arr = getlvstopwords()
  raksts.lower()
  return " ".join([word for word in str(raksts).split() if word not in stopwords_arr and word not in punct])

def tokenizacija(text):
    return [token.text for token in nlp(text)]

def tokenizacija_un_prieksapstrade(text):
    stopwords_arr = getlvstopwords()
    text_lower = text.lower()
    tokens = [token.text for token in nlp(text_lower) if token.text not in stopwords_arr and token.text not in punct]
    return tokens