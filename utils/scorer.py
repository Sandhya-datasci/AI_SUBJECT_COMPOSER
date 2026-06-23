import pickle
import pandas as pd

from utils.spam_detector import check_spam

model = pickle.load(
    open("models/subject_line_model.pkl", "rb")
)

def score_subject(text):

    df = pd.DataFrame({
        "length": [len(text)],
        "word_count": [len(text.split())],

        "has_urgent": [
            1 if "urgent" in text.lower() else 0
        ],

        "has_question": [
            1 if "?" in text else 0
        ],

        "has_exclusive": [
            1 if "exclusive" in text.lower() else 0
        ],

        "has_update": [
            1 if "update" in text.lower() else 0
        ],

        "has_application": [
            1 if "application" in text.lower() else 0
        ],

        "has_resume": [
            1 if "resume" in text.lower() else 0
        ],

        "has_candidate": [
            1 if "candidate" in text.lower() else 0
        ],

        "has_followup": [
            1 if "follow" in text.lower() else 0
        ]
    })

    score = model.predict(df)[0]

    return round(score, 2)


def rank_subjects(subjects):

    scored = []

    for s in subjects:

        score = score_subject(s)

        spam_status = check_spam(s)

        if str(spam_status).lower() != "safe":
            score -= 15

        scored.append(
            (s, round(score, 2))
        )

    scored.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scored