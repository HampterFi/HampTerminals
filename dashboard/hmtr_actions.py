import requests
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import concurrent.futures
import json 
import aiohttp
import asyncio
import logging
logging.basicConfig(level=logging.ERROR)


executor = ThreadPoolExecutor(max_workers=100)

async def pyth_process_market_pricing():
    try:
        url = "https://api.hampterfi.com/marketdata"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return 0
    except Exception as e:
        logging.info(f'Error occurred: {e}')
        
        