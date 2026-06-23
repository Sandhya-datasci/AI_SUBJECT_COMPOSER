import pickle

model = pickle.load(open("models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("models/intent_vectorizer.pkl", "rb"))

def detect_intent(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    return prediction