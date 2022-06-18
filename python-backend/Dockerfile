FROM python:3.10.1-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "app.py"]

