import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_product_page(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text


def extract_amazon_price(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")

    possible_ids = [
        "priceblock_ourprice",
        "priceblock_dealprice",
        "priceblock_saleprice",
    ]

    for element_id in possible_ids:
        tag = soup.find(id=element_id)
        if tag and tag.get_text(strip=True):
            return tag.get_text(strip=True)

    span = soup.find("span", class_="a-offscreen")
    if span and span.get_text(strip=True):
        return span.get_text(strip=True)

    return None


def extract_amazon_title(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find(id="productTitle")
    if title_tag:
        return title_tag.get_text(strip=True)
    return None
