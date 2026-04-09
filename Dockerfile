FROM python:3.12

WORKDIR /voloshyn

COPY . /voloshyn

RUN pip install -r requirements.txt

CMD ["python", "gtrans3.py"]