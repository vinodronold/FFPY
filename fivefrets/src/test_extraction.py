from celery import chain, group
from chords.tasks import download, extract, convert_to_chords

yt_id = 'IarsrX60bZw'

process_song = group([extract.s(),
                      convert_to_chords.s()])
d = chain(download.s(yt_id), process_song)()

# result = download.delay(yt_id)
# from datetime import datetime
# from chords.extraction import features

# print('START - ', datetime.now())
# y = features(yt_id="IarsrX60bZw")
# y = features(yt_id="4bZ-MAOLbGc")
# y.process_and_get_bpm()
# print(y.return_process_status, ' - ', y.id, ' - ', y.title)
# print('END - ', datetime.now())
