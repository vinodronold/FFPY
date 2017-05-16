from __future__ import print_function, unicode_literals
from fivefrets.settings import FF_EXTRACT_PATH, FF_EXTRACT_EXT, FF_EXTRACT_VAMP
from os import remove
from subprocess import check_call
from csv import reader
import youtube_dl
import librosa
# import traceback
# from chords.models import *


class features:
    """
        return_process_status
        ---------------------
        0  - SUCCESS
        1  - DURATION MORE THAN 8 MINUTE (480 sec)
        2  - DOWNLOAD ERROR
    """

    def __init__(self, yt_id):
        self.id = yt_id
        self.title = ''
        self.filepath = '/tmp/'
        self.ext = 'wav'
        self.vamp_plugin = 'nnls-chroma:chordino:simplechord'
        self.filenames = {
            'audio_path': self.filepath + self.id + '.' + self.ext,
            #'hpss_audio_path': self.filepath + self.id + '_hpss.' + self.ext,
            #'csv_path': self.filepath + self.id + '_hpss_vamp_' + self.vamp_plugin.replace(':', '_') + '.csv',
            'csv_path': self.filepath + self.id + '_vamp_' + self.vamp_plugin.replace(':', '_') + '.csv',
        }
        self.return_process_status = 0

    def download(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': self.ext,
            #'outtmpl': '%(id)s.%(ext)s',
            'outtmpl': self.filepath + '%(id)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.ext,
                'preferredquality': '128',
            }]
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        with ydl:
            try:
                result = ydl.extract_info(self.id, download=False)
                self.title = result['title']
                if (int(round(float(result['duration']))) > 480):
                    self.return_process_status = 1
                    return
                else:
                    ydl.download([self.id])
            except Exception as e:
                self.return_process_status = 2
                print("Can't process yt_id = ", self.id,
                      " %s\n" % traceback.format_exc())

    def extract(self):
        result = check_call([
            'sonic-annotator',
            '-d',
            'vamp:' + self.vamp_plugin,
            self.filenames['audio_path'],
            '-w', 'csv',
            '--csv-force',
            '--force',
        ])

    def convert_to_chords(self):
        try:
            audio, sample_rate = librosa.load(self.filenames['audio_path'])
            tempo, beat_frames = librosa.beat.beat_track(
                y=audio, sr=sample_rate)
            beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
            self.extract()

            with open(self.filenames['csv_path'], 'r') as f:
                chords = list(reader(f))
            print(chords[:10])

        except Exception as e:
            self.return_process_status = 3
            print("Can't process yt_id = %s" % self.id)
            # print("Can't process yt_id = ", self.id,
            #      " %s\n" % traceback.format_exc())

    def delete_all_files(self):
        for k, _file in self.filenames.items():
            remove(_file)

    def process_and_get_bpm(self):
        self.download()
        self.convert_to_chords()
        self.delete_all_files()
