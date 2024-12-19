FROM python:3.9-buster
ADD kostal_dashboard.py /
RUN pip3 install pymodbus psycopg2 influxdb-client
CMD [ "python3", "./kostal_dashboard.py" ]