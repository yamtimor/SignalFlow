from typing import List, Dict
from datetime import datetime
from sources.twelvedata_client import StockPrice  # <- adjust if needed

def transform_twelvedata(data: List[StockPrice]) -> List[Dict]:
    results = []

    for item in data:
        record = item.model_dump()
        record["timestamp"] = datetime.fromisoformat(item.datetime)
        record["source"] = "price"
        results.append(record)

    return results
