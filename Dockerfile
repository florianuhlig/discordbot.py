FROM python:3.9.13-slim-buster

WORKDIR /Bot

COPY pip-requirements.txt pip-requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r pip-requirements.txt

COPY . .

CMD ["python3", "bot.py"]