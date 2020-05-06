FROM python:3

ENV SLACK_API_TOKEN=xoxb-728627533346-1093301986486-BC2LnyuhPtbxOTmVYeLMh1Ss

WORKDIR /scrape
COPY . .
RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt
