FROM python:3.9-buster
ADD send_kostal_to_iothub.py /
ADD azure-iot-sdk-python /
RUN pip3 install azure-iot-device pymodbus psycopg2
CMD [ "python3", "./send_kostal_to_iothub.py" ]