import asyncio
import aiohttp
from logger import setup_logger

logger = setup_logger("AsyncFetcher")


class AsyncFetcher:
    """Fetch multiple URLs asynchronously using aiohttp."""

    def __init__(self, urls: list[str], retry: int = 2):
        self.urls = urls
        self.retry = retry

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> dict:
        """Fetch data from a single URL with retry capability."""
        for attempt in range(1, self.retry + 2):
            try:
                async with session.get(url, timeout=10) as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info(f"Success: {url}")
                    return {"url": url, "status": "success", "data": data}

            except Exception as e:
                logger.error(f"Attempt {attempt} failed for {url}: {e}")

            await asyncio.sleep(1)

        return {"url": url, "status": "failed", "data": {}}

    async def run(self) -> list:
        """Run fetch operations concurrently."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            return await asyncio.gather(*tasks)
