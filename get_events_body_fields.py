"""
Download sentry body fields as csv.
https://github.com/kevteg/sentry-body-fields
"""
import requests
import csv
import sys

if __name__ == '__main__':
    with open('data.csv', 'w', encoding='utf-8') as csvfile:
        issue_id = sys.argv[1] 
        auth = sys.argv[2]
        fieldnames = sys.argv[3:]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        url = "https://sentry.io/api/0/issues/{}/events/".format(issue_id)
        more_pages = True
        while more_pages:
            response = requests.get(
                url,
                headers={"Authorization": "Bearer {}".format(auth)})
            data = response.json()
            for event in data:
                payload = event['entries'][3]['data']['data']
                writer.writerow(dict(event, **payload))
            links = response.headers.get('Link').split()
            more_pages = "next" in links[5] and "true" in links[6]
            url = links[4][1:-2]
