from __future__ import print_function, unicode_literals
import datetime
import youtube_dl
import librosa
import traceback
import subprocess
import csv
from chords.models import *

class features:

    def __init__(self, yt_id):
        self.id = yt_id
        self.title = ''
        self.filepath = '/home/py/projects/tmp/'
        self.ext = 'wav'
        self.vamp_plugin = 'nnls-chroma:chordino:simplechord'

    def dowload(self):
        print("Start download - %s" % str(datetime.datetime.now()))
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio' : True,
            'audioformat' : self.ext,
            #'outtmpl': '%(id)s.%(ext)s',
            'outtmpl': self.filepath + '%(id)s.%(ext)s',
            'noplaylist' : True,
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
                result = ydl.extract_info(self.id, download=True)
                self.title = result['title']
            except Exception as e:
                print("Can't download audio! %s\n" % traceback.format_exc())

        #result = subprocess.check_call([
        #    'youtube-dl',
        #    '--no-playlist',
        #    '--extract-audio',
        #    '--audio-format', self.ext,
        #    '--output', self.filepath + '%(id)s.%(ext)s',
        #    '--cache-dir', self.filepath + 'youtube-dl',
        #    self.id,
        #    ])

    def extract(self):
        print("Start extract - %s" % str(datetime.datetime.now()))
        result = subprocess.check_call([
            'sonic-annotator',
            '-d',
            'vamp:'+self.vamp_plugin,
            self.filepath + self.id + '_hpss.' + self.ext,
            '-w', 'csv',
            '--csv-force',
            '--force',
            ])

    def process_beats(self):
        print("Start process_beats - %s" % str(datetime.datetime.now()))
        print('processing beats . . .')
        print('loading . . .')
        audio, sample_rate = librosa.load(self.filepath + self.id + '.' + self.ext)
        audio_harmonic, audio_percussive = librosa.effects.hpss(audio)
        print('get beat frames . . .')
        tempo, beat_frames = librosa.beat.beat_track(y=audio_percussive, sr=sample_rate)
        librosa.output.write_wav(self.filepath + self.id + '_hpss.' + self.ext, audio_harmonic, sample_rate)
        #print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
        print('beat frames to time . . .')
        beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
        #librosa.output.times_csv(self.filepath + self.id + '_librosa_beat_times.csv', beat_times)

        self.extract()
        print('load chords . . .')
        with open(self.filepath + self.id + '_vamp_' + self.vamp_plugin.replace(':', '_') + '.csv', 'r') as f:
            reader = csv.reader(f)
            chords = list(reader)

        #with open(self.filepath + self.id + '_librosa_beat_times.csv', 'r') as f:
        #    reader = csv.reader(f)
        #    beat_times = list(reader)

        print('match chords and beat . . .')
        chord_idx = 0

        # Adding Songs
        add_song = Song(name = self.title, youtube = self.id)
        add_song.save()
        insert_list = []

        for beat_time in beat_times:

            if float(beat_time) >= float(chords[chord_idx + 1][0]):
                chord_idx += 1

            est_chord = chords[chord_idx][1].split('-')
            id_chord_typ = ''
            if len(est_chord) > 1:
                id_chord_typ = est_chord[1]

            id_chords = Chord.objects.filter(name__exact = est_chord[0],
                                             typ__exact = 'MIN' if id_chord_typ == 'm' else 'MAJ')
            for id_chord in id_chords:
                id_chord = id_chord
                break
            insert_list.append(SongChord(song = add_song,
                                         chord = id_chord,
                                         beat_position = beat_time,
                                         start_time = chords[chord_idx][0]))
            # print(beat_time[0], chords[chord_idx][0], est_chord, id_chord, id_chord.id)

        SongChord.objects.bulk_create(insert_list)
