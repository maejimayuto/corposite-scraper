FROM python:3

WORKDIR /scrape
COPY . .
RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt
