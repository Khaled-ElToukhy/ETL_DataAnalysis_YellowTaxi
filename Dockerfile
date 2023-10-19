FROM python:3.9

RUN pip install pandas

RUN pip install sqlalchemy psycopg2

COPY titanic.csv titanic.csv

COPY yellow_tripdata_2021-01.csv yellow_tripdata_2021-01.csv

COPY taxi+_zone_lookup.csv taxi+_zone_lookup.csv

COPY ingest_ny_taxi.py ingest_ny_taxi.py

ENTRYPOINT ["python","ingest_ny_taxi.py"]






