from textblob import TextBlob
import pandas as pd

# sample reviews
reviews = [
    "This book is amazing",
    "Very bad experience",
    "I love this product",
    "Not good",
    "Excellent quality"
]

# empty list
sentiments = []

# loop through reviews
for review in reviews:

    # analyze text
    analysis = TextBlob(review)

    # get polarity
    polarity = analysis.sentiment.polarity

    # check sentiment
    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    # save result
    sentiments.append({
        "Review": review,
        "Polarity": polarity,
        "Sentiment": sentiment
    })

# create table
df = pd.DataFrame(sentiments)

# print result
print(df)

# save csv
df.to_csv("sentiment_analysis.csv", index=False)

print("\nSentiment Analysis Completed!")