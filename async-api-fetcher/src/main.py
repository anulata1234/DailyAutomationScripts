import asyncio
from fetcher import AsyncFetcher

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]

    fetcher = AsyncFetcher(urls)
    results = await fetcher.run()

    print("\nFinal Results:")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())
