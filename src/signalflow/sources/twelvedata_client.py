from dotenv import load_dotenv
import os
import aiohttp
from pydantic import BaseModel, Field 
from typing import Optional, List

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_API_KEY")
BASE_URL = "https://api.twelvedata.com/time_series"

class StockPrice(BaseModel):
    symbol: str
    datetime: str
    open: float
    high: float
    low: float
    close: float
    volume: int

async def fetch_stock_data(symbol: str, interval: str = "1min", outputsize: str = "5") -> List[StockPrice]:
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": API_KEY,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()

            if "values" not in data:
                raise Exception(f"Twelve Data API error: {data}")
            return [StockPrice(symbol=symbol, **v) for v in data["values"]]