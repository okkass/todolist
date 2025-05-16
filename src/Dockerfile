FROM python:3.12

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Expose the port the app runs on
EXPOSE 8000
CMD ["python", "main.py"]