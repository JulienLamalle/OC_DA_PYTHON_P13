FROM python:3.8.13-slim-buster
WORKDIR /app
ENV DEBUG=False  \
    PORT=8000
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:$PORT