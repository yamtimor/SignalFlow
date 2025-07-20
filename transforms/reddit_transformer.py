import re
from typing import List, Dict
from sources.reddit_client import RedditPost
from textblob import TextBlob

TICKER_PATTERN = r"\b[A-Z]{2,5}\b"  # crude: detects uppercase words 2–5 chars long


def extract_tickers_from_title(title: str) -> List[str]:
    return re.findall(TICKER_PATTERN, title)


def analyze_sentiment(text: str) -> float:
    blob = TextBlob(text)
    return blob.sentiment.polarity  # range from -1 to 1


def transform_reddit_posts(posts: List[RedditPost]) -> List[Dict]:
    results = []

    for post in posts:
        tickers = extract_tickers_from_title(post.title)
        sentiment = analyze_sentiment(post.title)

        for ticker in tickers:
            results.append({
                "ticker": ticker,
                "title": post.title,
                "score": post.score,
                "sentiment": sentiment,
                "created_utc": post.created_utc
            })

    return results
