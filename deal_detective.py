from scraper import fetch_product_page, extract_amazon_price


def normalize_url(url: str) -> str:
    """
    Make sure the URL has a scheme (http/https).
    If the user types 'amazon.com/...' we turn it into 'https://amazon.com/...'.
    """
    url = url.strip()

    if not url:
        return url

    # If it doesn't start with http:// or https://, assume https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def main() -> None:
    print("🕵️‍♂️ DealDetective – Amazon Price Checker (Prototype)")
    url = input("Enter an Amazon product URL: ").strip()

    if not url:
        print("No URL entered. Exiting.")
        return

    # 👇 Make the URL “smarter” by auto-adding https:// if needed
    url = normalize_url(url)

    try:
        html = fetch_product_page(url)
    except Exception as e:
        print(f"Error fetching page: {e}")
        return

    price = extract_amazon_price(html)

    if price:
        print(f"✅ Current price: {price}")
    else:
        print("⚠️ Could not find a price on this page. "
              "The HTML structure may have changed or this may not be a standard product page.")


if __name__ == "__main__":
    main()


title = extract_amazon_title(html)
if title:
    print(f"🛒 Product: {title}")
