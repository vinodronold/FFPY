from datetime import datetime
from chords.extraction import features

print('START - ', datetime.now())
y = features(yt_id="IarsrX60bZw")
#y = features(yt_id="4bZ-MAOLbGc")
y.process_and_get_bpm()
print(y.return_process_status, ' - ', y.id, ' - ', y.title)
print('END - ', datetime.now())
