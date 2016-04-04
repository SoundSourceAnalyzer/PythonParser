FROM humblehound/yaafe-docker

MAINTAINER Humblehound <dejtabejz@gmail.com>

#utils
RUN apt-get update && apt-get install -y \
	wget \
	unzip

#core
RUN apt-get update && apt-get install -y \
    python-numpy \
    python-scipy \
    python-pip

#json serialization
RUN pip install jsonpickle

CMD "mkdir app"
COPY parser.py app/
COPY wavfiles/* app/wavfiles/
WORKDIR app
EXPOSE 80
ENTRYPOINT ["python", "parser.py"]