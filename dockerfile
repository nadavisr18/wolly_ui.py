FROM python:3.8

COPY  ./communication ./communication
COPY  ./frontend ./frontend
COPY  main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.pydo"]