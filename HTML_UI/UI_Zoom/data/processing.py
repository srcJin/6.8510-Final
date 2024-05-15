import json


# Emotion mapping dictionaries
BASIC_TO_COMPLEX = {
    "anger": ["anger", "annoyance", "disapproval"],
    "fear": ["anxiety", "doubt", "fear", "horror"],
    "joy": [
        "admiration",
        "adoration",
        "amusement",
        "contentment",
        "desire",
        "ecstasy",
        "enthusiasm",
        "entrancement",
        "excitement",
        "gratitude",
        "joy",
        "love",
        "pride",
        "relief",
        "romance",
        "triumph",
    ],
    "sadness": [
        "disappointment",
        "distress",
        "empathic pain",
        "guilt",
        "nostalgia",
        "pain",
        "sadness",
    ],
    "surprise": [
        "awe",
        "confusion",
        "realization",
        "surprise (negative)",
        "surprise (positive)",
    ],
    "disgust": ["contempt", "disgust", "envy", "sarcasm"],
    "neutral": [
        "aesthetic appreciation",
        "awkwardness",
        "boredom",
        "calmness",
        "concentration",
        "contemplation",
        "craving",
        "determination",
        "embarrassment",
        "interest",
        "satisfaction",
        "shame",
        "sympathy",
        "tiredness",
    ],
}

SENTIMENT_TO_EMOTION = {
    "positive": [
        "admiration",
        "adoration",
        "aesthetic appreciation",
        "amusement",
        "awe",
        "contentment",
        "desire",
        "ecstasy",
        "enthusiasm",
        "entrancement",
        "excitement",
        "gratitude",
        "joy",
        "love",
        "pride",
        "relief",
        "romance",
        "triumph",
    ],
    "negative": [
        "anger",
        "annoyance",
        "anxiety",
        "awkwardness",
        "boredom",
        "contempt",
        "confusion",
        "craving",
        "disappointment",
        "disapproval",
        "disgust",
        "distress",
        "doubt",
        "empathic pain",
        "embarrassment",
        "envy",
        "fear",
        "guilt",
        "horror",
        "nostalgia",
        "pain",
        "sadness",
        "sarcasm",
        "shame",
        "surprise (negative)",
        "sympathy",
        "tiredness",
    ],
}
# # Load JSON data from file
with open("processed_results.json", "r") as file:
    data = json.load(file)


# Function to find basic and sentiment category for a given emotion
def map_emotions(emotions):
    basic_categories = {}
    sentiment_categories = {}

    for emotion, intensity in emotions.items():
        # Find basic category
        for basic, complex_emotions in BASIC_TO_COMPLEX.items():
            if emotion in complex_emotions:
                basic_categories[emotion] = basic
                break

        # Find sentiment category
        for sentiment, sentiment_emotions in SENTIMENT_TO_EMOTION.items():
            if emotion in sentiment_emotions:
                sentiment_categories[emotion] = sentiment
                break

    return basic_categories, sentiment_categories


# Processing each item in the data
results = []
for item in data:
    emotions = item["Top_Emotions"]
    basic_mapped, sentiment_mapped = map_emotions(emotions)
    results.append(
        {
            "Speaker": item["Speaker"],
            "Basic Categories": basic_mapped,
            "Sentiment Categories": sentiment_mapped,
        }
    )

# Display the results
for result in results:
    print(result)
