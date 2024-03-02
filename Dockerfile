FROM python:3.12-alpine3.19
ENV PHYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
RUN python3 -m pip install --upgrade pip
COPY . ./
RUN pip install -r requirements.txt
EXPOSE $PORT
ENV PORT=5000
COPY . /app
# CMD [ "python3","app.py" ]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app