FROM python:2

WORKDIR /usr/src/app

RUN mkdir -p /usr/src/app/external

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "setup.py", "install" ]
ENTRYPOINT ["python", "main.py"]
