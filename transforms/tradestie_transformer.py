from typing import List, Dict
from datetime import datetime
from sources.tradestie_client import SentimentData  # <- adjust if needed

def transform_tradestie(data: List[SentimentData]) -> List[Dict]:
    results = []

    for item in data:
        record = item.model_dump()
        record["timestamp"] = (
            datetime.fromisoformat(item.timestamp)
            if item.timestamp else datetime.utcnow()
        )
        record["source"] = "tradestie"
        record["sentiment_flag"] = (
            1 if item.sentiment.lower() == "bullish"
            else -1 if item.sentiment.lower() == "bearish"
            else 0
        )
        results.append(record)

    return results
