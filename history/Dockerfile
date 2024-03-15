FROM python:3

RUN apt-get update

#1. Install dependencies 
RUN apt-get install -y freetds-dev
RUN pip install --upgrade pip
RUN pip install cython
RUN pip install pymssql

#Copy and run my app
COPY . .
CMD [ "python", "history.py"]