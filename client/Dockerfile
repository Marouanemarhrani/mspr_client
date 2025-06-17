FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r client/requirements.txt

ENV PYTHONPATH=/app/client

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "client.wsgi:application"]
