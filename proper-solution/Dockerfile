FROM python:3.11

RUN mkdir -p /app
WORKDIR /app
COPY . /app

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python3", "./app-proper-solution.py"]