import asyncio
from sources.reddit_client import fetch_reddit_posts
from sources.tradestie_client import fetch_wsb_sentiment
from sources.twelvedata_client import fetch_stock_data
from pprint import pprint

SYMBOL = "VST" 

async def main():
    # data = await fetch_stock_data(SYMBOL)
    # print(f"Fetched {len(data)} data points for {SYMBOL}")
    # print(data[0].model_dump())  # Print first entry as dict
    # pprint(data)

    # wsb_sentiment = await fetch_wsb_sentiment()
    # print(f"\nWSB Sentiment — {len(wsb_sentiment)} tickers:")
    # pprint(wsb_sentiment)

    print("\n--- Top Reddit Posts ---")
    reddit_posts = await fetch_reddit_posts()
    for post in reddit_posts[:30]:  # show only top 5
        print(post.title)

if __name__ == "__main__":
    asyncio.run(main())