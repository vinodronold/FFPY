# APP BUILD
FROM ubuntu:16.04

ENV APP_ROOT /src
COPY ["./VAMP/nnls-chroma-1.1/nnls-chroma.*", "./VAMP/nnls-chroma-1.1/chord.dict", "./VAMP/sonic-annotator_1.4cc1-1_amd64.deb", "/usr/local/lib/vamp/"]
WORKDIR ${APP_ROOT}
RUN apt-get update && apt-get -y upgrade && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install dialog python3 python3-tk python3-pip libav-tools libfishsound1 libid3tag0 liblrdf0 libmad0 \
                          liboggz2 libqt5network5 libqt5xml5 libsamplerate0 libsndfile1 \
                          libsord-0-0 libsord-0-0 libstdc++6 vamp-plugin-sdk \
                          libfftw3-double3 libfishsound1 liblrdf0 libmad0 liboggz2 libqt5network5 libqt5xml5 \
                          libsamplerate0 libsndfile1 libsord-0-0 libid3tag0 libpq-dev\
    && dpkg -i "/usr/local/lib/vamp/sonic-annotator_1.4cc1-1_amd64.deb" \
    && rm "/usr/local/lib/vamp/sonic-annotator_1.4cc1-1_amd64.deb" \
    && pip3 install --upgrade pip \
    && pip3 install gunicorn \
    && pip3 install psycopg2 \
    && pip3 install django \
    && pip3 install celery \
    && pip3 install -U https://github.com/eventlet/eventlet/archive/f266be30f5c3ff1889e9ac3f0bad698a49d40e99.zip \
    && pip3 install dnspython \
    && pip3 install django-allauth \
    && pip3 install django-semanticui-form \
    && pip3 install numpy \
    && pip3 install librosa \
    && pip3 install --upgrade youtube_dl \
    && adduser --disabled-password --gecos '' ffrets
