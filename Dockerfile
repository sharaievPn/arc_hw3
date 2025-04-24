FROM python:3.10.1

WORKDIR /app
COPY ./app .

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
