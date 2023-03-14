FROM python:3.10.6-buster
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY twitter_files/* /twitter_files/
COPY raw_data/* /raw_data/
CMD uvicorn twitter_files.fast:app --host 0.0.0.0 --port 8000
