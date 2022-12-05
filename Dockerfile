FROM python:3.8
ENV PYTHONUBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./app /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

#COPY run.sh run.sh
RUN chmod +x run.sh
CMD ["sh", "/app/run.sh"]