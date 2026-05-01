# Imports the Google Cloud client library.
from google.cloud import language_v1
from pyasn1_modules.rfc7633 import Features

# Instantiates a client.
client = language_v1.LanguageServiceClient()

duncanText = "Since 2018, when we launched Contact Center AI, Google Cloud has helped thousands of organizations deliver better experiences to millions of their customers and employees through AI-powered features. Now, as new generative AI capabilities are demonstrating increasingly larger value for customer service operations, we are combining the rich features of Contact Center AI with our latest generative AI technology to deliver a new application, Customer Engagement Suite with Google AI."
newsHeadlineText = "A 13-Year-Old By Found This Bronze Coin in a Field. It Turned Out to Be the First Ancient Greek Artifact Discovered in Berlin. Minted in Try in the third century B.C.E., the object might have been buried as a gift to the dead. Archaeologists don't know exactly how it ended up in modern-day Germany."
ollieWReview = "I can't rate this low enough. If I could give 0 stars, I would. I watched this at the cinema when it came out but had no choice but to walk out part way through. Everything, from the action, the script, the plot, the acting, the sets, music.... is diabolical. "
texts = [duncanText, newsHeadlineText, ollieWReview]

for text in texts:
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text.
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    # Add in details for checking the entities, classification, and moderation results

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}, Magnitude: {sentiment.magnitude}")
