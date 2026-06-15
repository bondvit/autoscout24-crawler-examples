# Autoscout24 Crawler — examples

Runnable examples for the **[AutoScout24 Cars Scraper — EU Prices & Specs | from $1.39/1K](https://apify.com/bovi/autoscout24-cars-scraper)** on Apify.

Scrape AutoScout24 car listings across DE/FR/IT/NL/BE by make, model, price, year, mileage and fuel type. Returns 30+ fields: title, price, year, mileage, power, transmission, fuel, body type, seller info, location, images. Pay per result.

## What you get per record
see the actor's output schema on the Store page

## Quickstart
1. Get your Apify token: <https://console.apify.com/account/integrations>
2. Run a language example below. Both call the actor and print the results.

| Example | File |
|---|---|
| Python (`apify-client`) | [`examples/python/run.py`](examples/python/run.py) |
| JavaScript (`apify-client`) | [`examples/javascript/run.js`](examples/javascript/run.js) |

## Example input
```json
{
  "make": "volkswagen",
  "model": "golf",
  "country": "D",
  "maxItems": 100,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ],
    "apifyProxyCountry": "DE"
  }
}
```

## Links
- **Actor on Apify Store:** <https://apify.com/bovi/autoscout24-cars-scraper>
- **Apify client docs:** [Python](https://docs.apify.com/api/client/python/) · [JavaScript](https://docs.apify.com/api/client/js/)

---
_MIT-licensed examples. The actor runs on the caller's Apify account (you pay platform compute + per-result)._
