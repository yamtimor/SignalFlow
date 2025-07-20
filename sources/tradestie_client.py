import aiohttp
from typing import List, Optional
from pydantic import BaseModel


class SentimentData(BaseModel):
    ticker: str
    sentiment: str  # It's "Bullish", "Bearish", or similar — not a float
    no_of_comments: Optional[int] = 0
    sentiment_score: Optional[float] = None
    sentiment_score_scaled: Optional[float] = None
    timestamp: Optional[str] = None  # Sometimes missing


API_URL = "https://tradestie.com/api/v1/apps/reddit"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


async def fetch_wsb_sentiment() -> List[SentimentData]:
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(API_URL) as response:
            if response.status != 200:
                text = await response.text()
                raise Exception(f"Status {response.status}: {text[:100]}...")

            data = await response.json()

            if not isinstance(data, list):
                raise ValueError(f"Unexpected API response: {data}")

            return [SentimentData(**item) for item in data]
