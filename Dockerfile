FROM python:3.10-slim

RUN mkdir /app

COPY . ./app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



RUN pip install --upgrade pip && \
    pip install -r /app/server_simple_gram/requirements.txt --no-cache-dir



WORKDIR /app/server_simple_gram/backend/bot_django_project

COPY server_simple_gram/backend/bot_django_project/entrypoint.sh .

RUN sed -i 's/\r$//g' /app/server_simple_gram/backend/bot_django_project/entrypoint.sh
RUN chmod +x /app/server_simple_gram/backend/bot_django_project/entrypoint.sh


ENTRYPOINT ["/app/server_simple_gram/backend/bot_django_project/entrypoint.sh"]
