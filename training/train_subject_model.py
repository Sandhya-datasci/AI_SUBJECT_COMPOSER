import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/subject_line_dataset.csv")

# -----------------------------
# Feature Engineering
# -----------------------------

df["length"] = df["subject_line"].apply(len)

df["word_count"] = df["subject_line"].apply(
    lambda x: len(str(x).split())
)

df["has_urgent"] = df["subject_line"].str.contains(
    "urgent", case=False, na=False
).astype(int)

df["has_question"] = df["subject_line"].str.contains(
    r"\?", na=False
).astype(int)

df["has_exclusive"] = df["subject_line"].str.contains(
    "exclusive", case=False, na=False
).astype(int)

df["has_update"] = df["subject_line"].str.contains(
    "update", case=False, na=False
).astype(int)

df["has_application"] = df["subject_line"].str.contains(
    "application", case=False, na=False
).astype(int)

df["has_resume"] = df["subject_line"].str.contains(
    "resume", case=False, na=False
).astype(int)

df["has_candidate"] = df["subject_line"].str.contains(
    "candidate", case=False, na=False
).astype(int)

df["has_followup"] = df["subject_line"].str.contains(
    "follow", case=False, na=False
).astype(int)

# -----------------------------
# Features
# -----------------------------

X = df[
    [
        "length",
        "word_count",
        "has_urgent",
        "has_question",
        "has_exclusive",
        "has_update",
        "has_application",
        "has_resume",
        "has_candidate",
        "has_followup"
    ]
]

y = df["open_rate"]

# -----------------------------
# Train/Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Save Model
# -----------------------------

pickle.dump(
    model,
    open("models/subject_line_model.pkl", "wb")
)

print("✅ Subject Model Saved")