# APP BUILD
FROM python:3.5

ENV PYTHONUNBUFFERED 1
ENV APP_DEBUG True
ENV APP_USER fivefrets
ENV APP_SECRET_KEY fcoh)7w^p@hyb1t4&=et74@ue2^0hav01qb5d956cay7@hn*ce
ENV APP_ROOT /src

RUN mkdir /src \
    && mkdir /usr/local/lib/vamp \
    && groupadd -r ${APP_USER} \
    && useradd -r -m --home-dir ${APP_ROOT} -s /usr/sbin/nologin -g ${APP_USER} ${APP_USER} \
    && apt-get update \
    && apt-get -y upgrade \
    && pip install --upgrade pip \
    && pip install django \
    && pip install gunicorn \
    && pip install psycopg2 \
    && pip install numpy \
    && pip install librosa \
    && pip install --upgrade youtube_dl \
    && apt-get -y install libfishsound1 libid3tag0 liblrdf0 libmad0 liboggz2 libqt5network5 libqt5xml5 libsamplerate0 libsndfile1 libsord-0-0 libsord-0-0 \
    && wget "https://code.soundsoftware.ac.uk/attachments/download/1876/sonic-annotator_1.4cc1-1_amd64.deb" -qO "sonic_annotator" \
    && dpkg -i "sonic_annotator" \
    && apt-get -f install \
    && rm "sonic_annotator"

COPY ["./VAMP/nnls-chroma-1.1/nnls-chroma.*", "./VAMP/nnls-chroma-1.1/chord.dict", "/usr/local/lib/vamp/"]

WORKDIR ${APP_ROOT}
ADD ./src/start.sh /
USER ${APP_USER}
ADD . ${APP_ROOT}
