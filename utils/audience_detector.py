import pickle

model = pickle.load(open("models/audience_model.pkl", "rb"))
vectorizer = pickle.load(open("models/audience_vectorizer.pkl", "rb"))

def detect_audience(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    return prediction