import aiohttp
import asyncio 
from bs4 import BeautifulSoup

from app.utils.logging import logger
from app.utils.file_work import save_json
from core.config import config


class WebCrawler:
    def __init__(self, urls: list[str]) -> None:
        self.__init_checker(urls)

        self.urls = urls

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/125.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        self.Semaphore = asyncio.Semaphore(2)

    def __init_checker(self, paths: list[str]) -> None | Exception:
        for path in paths:
            if not isinstance(path, str):
                logger.error(f"TypeError with {path}")
                raise TypeError(f"Wrong type for {path}: {type(str)}")

    def __save_results(self, data_list: list[tuple]) -> None:
        result = []
        
        for data in data_list:
            result.append(
                {
                    "url"    : data[0],
                    "status" : data[1],
                    "title"  : data[2]
                }
            )

        save_json(config['PATH']['RESULT_FILE'], result)

    async def parse_info(self, html: str, info: str) -> str | None:
        try: 
            soap = BeautifulSoup(html, 'html.parser')     
            title = soap.find(info)

            return title.text
        except: 
            return None
    
    async def fetch(self, url: str) -> tuple[int, str]:
        try: 
            timeout = aiohttp.ClientTimeout(total=5)

            async with aiohttp.ClientSession(
                headers=self.headers, timeout=timeout
                ) as session:
                async with session.get(url) as response:
                    html = await response.text()

                    if response.status == 200:
                        title = await self.parse_info(html, 'title')  
                    else:
                        title = None

                    return url, title, response.status
        except Exception as e:
            logger.error(e)
            return url, None, "Error"

    async def main(self) -> None:
        
        async def fetch_with_semaphore(url) -> tuple[int, str]:
            async with self.Semaphore:
                await asyncio.sleep(0.5)
                
                try: 
                    url, title, status =  await self.fetch(url)
                    return url, title, status 
                except Exception as e:
                    logger.error(e)
                    return url, None, "Error"
            
        tasks = [fetch_with_semaphore(url) for url in self.urls]
        results = await asyncio.gather(*tasks)

        self.__save_results(results)

    def start(self) -> None:
        asyncio.run(self.main())