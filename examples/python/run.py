"""
autoscout24-cars-scraper — Python example.

    pip install apify-client
    export APIFY_TOKEN=...        # https://console.apify.com/account/integrations
    python run.py

Docs: https://apify.com/bovi/autoscout24-cars-scraper
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {   'make': 'volkswagen',
    'model': 'golf',
    'country': 'D',
    'maxItems': 100,
    'proxyConfiguration': {   'useApifyProxy': True,
                              'apifyProxyGroups': ['RESIDENTIAL'],
                              'apifyProxyCountry': 'DE'}}

run = client.actor("bovi/autoscout24-cars-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
