FROM python:3.8

ADD src /
ADD requirements.txt /

RUN pip install -r requirements

CMD [ "python", "-m", "src"]