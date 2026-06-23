import pickle

model = pickle.load(open("models/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("models/spam_vectorizer.pkl", "rb"))

def check_spam(text):

    text_lower = text.lower()

    # Safe job-related keywords
    safe_keywords = [
        "application",
        "resume",
        "internship",
        "position",
        "candidate",
        "job",
        "hiring",
        "role",
        "cv"
    ]

    for word in safe_keywords:
        if word in text_lower:
            return "safe"

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    return prediction