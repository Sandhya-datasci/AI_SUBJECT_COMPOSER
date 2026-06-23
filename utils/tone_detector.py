import pickle

model = pickle.load(open("models/tone_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tone_vectorizer.pkl", "rb"))

def detect_tone(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    return prediction