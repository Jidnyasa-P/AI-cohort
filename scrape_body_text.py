import requests
from bs4 import BeautifulSoup

url = "https://www.healthcare.gov/coverage/whats-covered/"
resp = requests.get(url, timeout=20)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

candidates = [
    soup.select_one("main"),
    soup.select_one("article"),
    soup.select_one("div#main-content"),
    soup.select_one("div#content"),
    soup.select_one("div[class*=content]"),
    soup.select_one("div[class*=page]"),
]

body = None
for cand in candidates:
    if cand:
        text = cand.get_text(separator="\n", strip=True)
        if len(text) > 400:
            body = text
            print(f"Using selector: {cand.name} {cand.get('id') or cand.get('class')}\n")
            break

if body is None:
    # fallback: collect large sections and filter
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
    body = "\n\n".join(paragraphs[:30])
    print("Using fallback paragraph extraction\n")

print(body[:4000])
