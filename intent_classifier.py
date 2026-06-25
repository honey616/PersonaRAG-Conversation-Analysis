from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Small offline dataset

train_texts = [

    "remind me tomorrow",
    "set reminder at 5 pm",

    "i feel sad",
    "i am stressed",

    "submit the report",
    "complete assignment",

    "hello",
    "good morning",

    "what is this"
]

train_labels = [

    "reminder",
    "reminder",

    "emotional-support",
    "emotional-support",

    "action-item",
    "action-item",

    "small-talk",
    "small-talk",

    "unknown"
]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(train_texts, train_labels)


def classify_intent(message):

    return model.predict([message])[0]


if __name__ == "__main__":

    msg = input("Enter Message: ")

    print("Intent:", classify_intent(msg))