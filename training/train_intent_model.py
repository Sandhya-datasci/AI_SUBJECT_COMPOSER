import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("data/email_body_dataset.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["email_body"])
y = df["intent"]

model = MultinomialNB()
model.fit(X, y)

pickle.dump(model, open("models/intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/intent_vectorizer.pkl", "wb"))

print("Intent Model Saved")