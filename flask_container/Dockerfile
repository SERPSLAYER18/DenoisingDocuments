# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

#WORKDIR /python-docker
RUN python -m pip install --upgrade pip

RUN pip3 install tensorflow==2.6.0
RUN pip3 install keras==2.6
RUN apt-get update \
    && apt-get install ffmpeg \libsm6 libxext6  -y
RUN apt-get install libleptonica-dev \
                    tesseract-ocr \
                    libtesseract-dev \
                    python3-pil \
                    tesseract-ocr-eng \
                    tesseract-ocr-script-latn -y
RUN pip3 install pytesseract
#RUN pip3 install pytesseract-ocr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#RUN apt-get install mysql-client
#RUN apt-get install python-mysqldb -y
RUN pip3 install psycopg2-binary
EXPOSE 5000

COPY .. .

ENV FLASK_APP=App/__init__.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
#CMD ["apt-get" ,"update"]
#CMD ["apt-get", "install" ,"ffmpeg", "libsm6" ,"libxext6" , "-y"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]