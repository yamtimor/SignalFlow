import aiohttp
from typing import List
from pydantic import BaseModel


class RedditPost(BaseModel):
    title: str
    score: int
    created_utc: float  # timestamp in UNIX format


URL = "https://www.reddit.com/r/wallstreetbets/top.json?limit=50&t=day"

HEADERS = {
    "User-Agent": "wsb-stock-analyzer/0.1 by yamtimor"
}


async def fetch_reddit_posts() -> List[RedditPost]:
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL) as response:
            if response.status != 200:
                text = await response.text()
                raise Exception(f"Status {response.status}: {text[:100]}...")

            data = await response.json()
            posts = data.get("data", {}).get("children", [])
            results = []

            for post in posts:
                post_data = post.get("data", {})
                results.append(
                    RedditPost(
                        title=post_data.get("title", ""),
                        score=post_data.get("score", 0),
                        created_utc=post_data.get("created_utc", 0.0),
                    )
                )

            return results
