FROM python:3

ENV SLACK_API_TOKEN=

WORKDIR /scrape
COPY . .
RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt
