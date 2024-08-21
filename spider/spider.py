import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
import json

my_dict = {}
lock = asyncio.Lock()

async def safe_add_to_dict(key, value):
    async with lock:
        my_dict[key] = value


class WebCrawler:
    def __init__(self, urls):
        self.urls = urls
        self.visited_urls = set()

    async def fetch_url(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def parse_response(self, response_text):
        out={}
        # 在这里使用 BeautifulSoup 或其他解析库解析 response_text
        soup = BeautifulSoup(response_text, 'html.parser')

        p = re.compile(r"<li><span>(.+)</span></li>")

        # print(soup.text)
        #穴位名
        #text = re.findall(p, str(soup))
        #for i in text:
            #print(i)
        h1=soup.find_all("h1")
        if("《针灸学》" not in h1[0].text):
            #print(h1[0].text)
            p = soup.find_all("p")
            strr=""
            for i in p:
                if "img" in str(i) or 'h1' in str(i):
                    continue
                #print(i.text)
                strr+=i.text+"%"
            await safe_add_to_dict(h1[0].text,strr)

    async def crawl(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls:
                if url not in self.visited_urls:
                    self.visited_urls.add(url)
                    tasks.append(self.fetch_url(session, url))

            responses = await asyncio.gather(*tasks)

            for url, response_text in zip(self.urls, responses):
                title = await self.parse_response(response_text)
                #print(f"Title of {url}: {title}")

if __name__ == "__main__":
    baseurl = 'https://www.zysj.com.cn/lilunshuji/zhenjiuxue/'
    urls = [baseurl + str(i) + '.html' for i in range(2767, 3239)]
    crawler = WebCrawler(urls)
    asyncio.run(crawler.crawl())

    print(my_dict)
    with open ("aaaa.txt","w",encoding="UTF8") as f :
        f.write(json.dumps(my_dict,indent=4).encode().decode("unicode_escape"))
