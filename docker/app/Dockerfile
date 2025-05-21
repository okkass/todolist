FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip

COPY src/requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]