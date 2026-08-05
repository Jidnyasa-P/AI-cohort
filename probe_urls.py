import requests

urls = [
    'https://www.cdc.gov/healthinsurance/index.html',
    'https://www.cms.gov/coverage',
    'https://www.bluecrossma.org/individuals-families/coverage-and-costs',
    'https://www.insure.com/health-insurance/',
]
headers = {'User-Agent': 'Mozilla/5.0'}
for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=20)
        print(url, r.status_code, len(r.text))
    except Exception as e:
        print(url, 'ERR', e)
