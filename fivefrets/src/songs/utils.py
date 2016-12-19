from fivefrets.settings import FF_YT
import requests


def validate_ytid(ytid=None):
    if ytid:
        r = requests.get(FF_YT['API_URL'] + FF_YT['VIDEO'], params={
            'part': 'id',
            'key': FF_YT['API_KEY'],
            'id': ytid
        })
        items = r.json()['items']
        print('items', items)

        return (items[0]['id'] == ytid if (r.status_code == 200 and items) else False)
    else:
        return
