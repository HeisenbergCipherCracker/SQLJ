FROM python:3.11
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app
CMD python sql.py

