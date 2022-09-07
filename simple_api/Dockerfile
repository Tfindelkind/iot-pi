FROM python:3.9-buster
ADD simple_api.py /
RUN pip3 install flask
ENV FLASK_APP=simple_api.py
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]