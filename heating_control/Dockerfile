FROM python:3.9-buster
ADD hc.py /
RUN pip3 install pymodbus psycopg2
CMD [ "python3", "./hc.py" ]