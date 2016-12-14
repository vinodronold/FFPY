from fivefrets.settings import FF_YT
import requests


def validate_ytid(ytid=None):
    if ytid:
        r = requests.get(FF_YT['API_URL'], params={
            'part': 'id',
            'key': FF_YT['API_KEY'],
            'id': ytid
        })
    else:
        return
