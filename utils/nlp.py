import re
from rake_nltk import Rake
from textblob import TextBlob

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:10]

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity
