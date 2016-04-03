FROM philcryer/min-wheezy

MAINTAINER Humblehound <dejtabejz@gmail.com>

RUN apt-get update && apt-get install -y \
    python-numpy \
    python-scipy \
    python-pip

RUN pip install jsonpickle

CMD "mkdir app"
COPY parser.py app/
COPY wavfiles/* app/wavfiles/
WORKDIR app

ENTRYPOINT ["python", "parser.py"]