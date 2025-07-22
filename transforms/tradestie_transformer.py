from typing import List, Dict
from datetime import datetime, timezone
from sources.tradestie_client import SentimentData  # adjust import path

def transform_tradestie(data: List[SentimentData]) -> List[Dict]:
    results = []

    for item in data:
        record = item.model_dump()
        record["timestamp"] = (
            datetime.fromisoformat(item.timestamp).astimezone(timezone.utc)
            if item.timestamp
            else datetime.now(timezone.utc)
        )
        record["source"] = "tradestie"
        record["sentiment_flag"] = (
            1 if item.sentiment.lower() == "bullish"
            else -1 if item.sentiment.lower() == "bearish"
            else 0
        )
        results.append(record)

    return results
