# classify_new_tweets.py
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

# Download stopwords if not already available
nltk.download('stopwords')

# Load the saved model and vectorizer
model = pickle.load(open('trained_model.sav', 'rb'))
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))

# Preprocessing function
def preprocess_tweet(content):
    port_stem = PorterStemmer()
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [port_stem.stem(word) for word in content if word not in stopwords.words('english')]
    return ' '.join(content)

# Function to classify a new tweet
def classify_tweet(tweet):
    processed_tweet = preprocess_tweet(tweet)
    transformed_tweet = vectorizer.transform([processed_tweet])
    prediction = model.predict(transformed_tweet)
    return "Positive" if prediction == 1 else "Negative"

# Example usage
if __name__ == "__main__":
    new_tweet = input("Enter a tweet to classify: ")
    sentiment = classify_tweet(new_tweet)
    print(f"Tweet: {new_tweet}")
    print(f"Sentiment: {sentiment}")
