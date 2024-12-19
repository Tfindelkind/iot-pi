FROM python:3.9-buster
ADD kostal_dashboard.py /
RUN pip3 install pymodbus==3.1.1 psycopg2 influxdb-client
CMD [ "python3", "./kostal_dashboard.py" ]