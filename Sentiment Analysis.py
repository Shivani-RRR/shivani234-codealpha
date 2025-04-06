from textblob import TextBlob

# Example text
text = "I love this product! It's amazing and works great."

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Positive sentiment")
elif sentiment < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Example text
text = "I hate this! It's the worst purchase I've ever made."

# Get sentiment scores
sentiment_scores = analyzer.polarity_scores(text)

# Analyze sentiment
if sentiment_scores['compound'] >= 0.05:
    print("Positive sentiment")
elif sentiment_scores['compound'] <= -0.05:
    print("Negative sentiment")
else:
    print("Neutral sentiment")

import matplotlib.pyplot as plt

sentiments = ['Positive', 'Negative', 'Neutral']
counts = [50, 30, 20]  # Example sentiment count

plt.bar(sentiments, counts, color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.show()

texts = ["I love this product!", "This is terrible.", "It’s okay, nothing special."]
sentiments = []

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiments.append("Positive")
    elif sentiment < 0:
        sentiments.append("Negative")
    else:
        sentiments.append("Neutral")

print(sentiments)

reviews = [
    "This product is amazing! Highly recommend it.",
    "Worst purchase I’ve ever made. Waste of money.",
    "It’s okay, not the best but does the job."
]

from textblob import TextBlob

sentiments = []
for review in reviews:
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiments.append("Positive")
    elif sentiment < 0:
        sentiments.append("Negative")
    else:
        sentiments.append("Neutral")

print(sentiments)  # Output: ['Positive', 'Negative', 'Neutral']

import matplotlib.pyplot as plt

sentiment_counts = {'Positive': 1, 'Negative': 1, 'Neutral': 1}

plt.bar(sentiment_counts.keys(), sentiment_counts.values())
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.title('Sentiment Analysis of Product Reviews')
plt.show()
