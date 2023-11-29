FROM python:3.11-alpine

ENV PYENV=1
ENV PYENV=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
