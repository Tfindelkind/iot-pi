FROM python:3

RUN apt-get update

#1. Install dependencies 
RUN apt-get install -y freetds-dev
RUN pip install --upgrade pip
RUN pip install cython
RUN pip install pymssql

#Copy and run my app
COPY . .
<<<<<<< HEAD
CMD [ "python", "create_history.py"]
=======
CMD [ "python", "history.py"]
>>>>>>> 68e6ed537811fe953d29b5843d5569517e0f09ff
