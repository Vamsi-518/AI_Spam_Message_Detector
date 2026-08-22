from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    "Congratulations you won a free prize",
    "Win money now click this link",
    "You have won a lottery",
    "Get free recharge today",
    "Claim your free gift",
    "Free cash available click now",
    "You are selected for a cash prize",
    "Win a brand new phone",
    "Click here to claim your reward",
    "Congratulations you are a winner",

    "Hello how are you",
    "Can we meet tomorrow",
    "Please send me the project",
    "What time is the meeting",
    "I will call you later",
    "Let's go for lunch",
    "Your order has been delivered",
    "Please send the documents",
    "Good morning",
    "How was your day"
]

labels = [
    "spam", "spam", "spam", "spam", "spam",
    "spam", "spam", "spam", "spam", "spam",

    "normal", "normal", "normal", "normal", "normal",
    "normal", "normal", "normal", "normal", "normal"
]

# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(messages)

# Create and train AI model
model = MultinomialNB()
model.fit(X, labels)


def predict_message(message):
    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)[0]

    probability = model.predict_proba(message_vector).max()

    return prediction, round(probability * 100, 2)