FROM python:3.12-alpine3.19
WORKDIR /app
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app
CMD [ "python3","app.py" ]