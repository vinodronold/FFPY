from __future__ import absolute_import, unicode_literals
from fivefrets.settings import (FF_EXTRACT_PATH, FF_EXTRACT_EXT, FF_EXTRACT_YTID,
                                FF_EXTRACT_VAMP, FF_EXTRACT_FILEPATH, FF_EXTRACT_CSV, FF_EXTRACT_MAX_DURATION)
from fivefrets.celery import app
from songs.utils import validate_ytid
from songs.models import Song, SongChord


def resolve_filepath(filepath, ytid):
    return str(filepath.replace(FF_EXTRACT_YTID, ytid))


@app.task
def download(ytid):
    song = Song.objects.get(youtube=ytid)
    if validate_ytid(ytid=ytid):
        from youtube_dl import YoutubeDL
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': FF_EXTRACT_EXT,
            'outtmpl': FF_EXTRACT_PATH + '%(id)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': FF_EXTRACT_EXT,
                'preferredquality': '128',
            }]
        }
        ydl = YoutubeDL(ydl_opts)
        with ydl:
            try:
                result = ydl.extract_info(ytid, download=False)
                if (int(round(float(result['duration']))) > FF_EXTRACT_MAX_DURATION):
                    song.process_status = 3
                    song.save()
                    ytid = None
                else:
                    ydl.download([ytid])
                    song.process_status = 2
                    song.name = result['title']
                    song.save()
            except Exception as e:
                print("Can't process yt_id = %s" % ytid)
            return ytid
    else:
        song.process_status = 6
        song.name = 'Invalid'
        song.save()
        ytid = None
        return


@app.task
def extract(ytid):
    if ytid:
        from subprocess import check_call
        result = check_call([
            'sonic-annotator',
            '-d',
            'vamp:' + FF_EXTRACT_VAMP,
            resolve_filepath(FF_EXTRACT_FILEPATH, ytid),
            '-w', 'csv',
            '--csv-force',
            '--force',
        ])
    return ytid


@app.task
def convert_to_chords(ytid):
    if ytid:
        from librosa import load, beat, frames_to_time
        try:
            audio, sample_rate = load(
                resolve_filepath(FF_EXTRACT_FILEPATH, ytid))
            tempo, beat_frames = beat.beat_track(y=audio, sr=sample_rate)
            beat_times = frames_to_time(beat_frames, sr=sample_rate)
        except Exception as e:
            print("Can't process yt_id = %s" % ytid)
    return save_chords(ytid, '{:.2f}'.format(tempo), beat_times) if ytid else None


def save_chords(ytid, beat_per_min, beat_times):
    if ytid:
        from csv import reader
        from chords.models import Chord
        song = Song.objects.get(youtube=ytid)
        with open(resolve_filepath(FF_EXTRACT_CSV, ytid), 'r') as f:
            chords = list(reader(f))
        chord_idx = 0
        insert_list = []
        for beat_time in beat_times:
            chord_idx = chord_idx = chord_idx + \
                1 if float(beat_time) >= float(
                    chords[chord_idx + 1][0]) else chord_idx
            est_chord = chords[chord_idx][1].split('-')
            id_chord_typ = est_chord[1] if len(est_chord) > 1 else None
            id_chords = Chord.objects.filter(name__exact=est_chord[0],
                                             typ__exact='MIN' if id_chord_typ == 'm' else 'MAJ')
            for id_chord in id_chords:
                id_chord = id_chord
                break

            insert_list.append(SongChord(song=song,
                                         chord=id_chord,
                                         beat_position=beat_time,
                                         start_time=chords[chord_idx][0]))
        SongChord.objects.bulk_create(insert_list)
        song.bpm = beat_per_min
        song.process_status = 0
        song.save()

    return ytid


@app.task
def delete_all_files(ytid):
    if ytid:
        from os import remove
        remove(resolve_filepath(FF_EXTRACT_FILEPATH, ytid))
        remove(resolve_filepath(FF_EXTRACT_CSV, ytid))
