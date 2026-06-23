import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/spam_dataset.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["subject_line"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("models/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/spam_vectorizer.pkl", "wb"))

print("Spam Model Saved")