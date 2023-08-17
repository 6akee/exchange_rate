import aiohttp
from fastapi import APIRouter

from app.core import config

router = APIRouter()


async def get_currency_rates():
    url = f"http://api.coinlayer.com/api/live?access_key={config.settings.EXCHANGE_API}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    return data


@router.post("/currency_rates")
async def currency_rates():
    rates = await get_currency_rates()
    return rates
