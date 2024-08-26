import aiohttp
import asyncio
from bs4 import BeautifulSoup

class TravelReviewScraper:
    def __init__(self, base_url, max_pages=48):
        self.base_url = base_url
        self.max_pages = max_pages

    async def fetch_page(self, session, page_number):
        url = f"{self.base_url}page/{page_number}/"
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            review_blocks = soup.find_all("article", {"itemprop": "review"})
            reviews = [(block.find('div', class_='text_content').get_text(strip=True),
                        block.find('time').get_text(strip=True)) for block in review_blocks]
            return reviews

    async def fetch_reviews(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_page(session, page_number) for page_number in range(1, self.max_pages + 1)]
            all_reviews = await asyncio.gather(*tasks)
            return [review for reviews in all_reviews for review in reviews]  # Flatten

def scrape_reviews():
    base_url = 'https://www.airlinequality.com/airline-reviews/kenya-airways/'
    scraper = TravelReviewScraper(base_url)
    return asyncio.run(scraper.fetch_reviews())
