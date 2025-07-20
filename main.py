import asyncio
from sources.twelvedata_client import fetch_stock_data
from pprint import pprint

SYMBOL = "VST" 

async def main():
    data = await fetch_stock_data(SYMBOL)
    print(f"Fetched {len(data)} data points for {SYMBOL}")
    # print(data[0].model_dump())  # Print first entry as dict
    pprint(data)
if __name__ == "__main__":
    asyncio.run(main())