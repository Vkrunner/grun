FROM python:3.12-alpine3.19
ENV APP_HOME /app
WORKDIR $APP_HOME
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE $PORT
ENV PORT=5000
COPY . /app
CMD [ "python3","app.py" ]