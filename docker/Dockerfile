FROM python:3.11

WORKDIR /app
COPY requirements.txt .
COPY packages .
COPY ipcalc_bot.py .
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["python3", "./ipcalc_bot.py"]
