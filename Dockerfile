FROM python:3.8.1-alpine3.11
        COPY *.py /
        COPY *.txt /
        RUN pip install -r requirements.txt
 
        CMD python MainGame.py
