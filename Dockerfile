FROM philcryer/min-wheezy

MAINTAINER Humblehound <dejtabejz@gmail.com>

RUN apt-get update && apt-get install -y \
    python-numpy \
    python-scipy \
    python-pip \
    wget \
    unzip

RUN pip install jsonpickle

# install dependencies-
RUN mkdir downloads
RUN wget --no-check-certificate https://github.com/jameslyons/python_speech_features/archive/master.zip
RUN unzip master.zip -d /downloads/
RUN cd /downloads/python_speech_features-master/ && python setup.py install

CMD "mkdir app"
COPY parser.py app/
COPY wavfiles/* app/wavfiles/
WORKDIR app

ENTRYPOINT ["python", "parser.py"]