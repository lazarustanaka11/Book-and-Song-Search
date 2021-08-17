FROM python:3-onbuild

COPY . /usr/src/app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD [ "interface.py" ]