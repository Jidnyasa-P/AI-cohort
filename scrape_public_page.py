import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
urls = [
    "https://www.cdc.gov/healthinsurance/index.html",
    "https://www.bcbs.com/faq",
    "https://www.uhc.com/individual-and-family/health-insurance/plans",
    "https://www.insure.com/health-insurance/",
]

for url in urls:
    print(f"\n=== Trying {url} ===")
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        print("status", resp.status_code)
    except Exception as exc:
        print("fetch error", exc)
        continue
    if resp.status_code != 200:
        continue

    soup = BeautifulSoup(resp.text, "html.parser")
    candidate = None
    selectors = [
        "main",
        "article",
        "div#main-content",
        "div#content",
        "div[class*=content]",
        "div[class*=page]",
        "div[class*=container]",
        "section",
    ]
    for sel in selectors:
        el = soup.select_one(sel)
        if not el:
            continue
        text = el.get_text(separator="\n", strip=True)
        print(f"selector {sel} len {len(text)}")
        if len(text) > 600:
            candidate = (sel, text)
            break
    if candidate:
        sel, text = candidate
        print(f"Selected {url} with {sel} (len {len(text)})")
        print(text[:4000])
        break
    print("no good main text candidate")
