FROM python:3.9-buster
ADD hc.py /
RUN pip3 install pymodbus psycopg2 RPi.GPIO
CMD [ "python3","-u","./hc.py" ]