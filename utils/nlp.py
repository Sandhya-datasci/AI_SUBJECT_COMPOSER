import re
import nltk
from rake_nltk import Rake
from textblob import TextBlob

# Download NLTK resources only if they are missing
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# For newer NLTK versions (used by some deployments)
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    try:
        nltk.download("punkt_tab")
    except:
        pass


def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()


def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:10]


def get_sentiment(text):
    return TextBlob(text).sentiment.polarity