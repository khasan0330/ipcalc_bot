FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
VOLUME /var/log/

CMD ["python3", "./ipcalc_bot.py"]
