FROM python:3.11
COPY . /app
RUN pip install requests
WORKDIR /app
CMD python SQLJng.py 

