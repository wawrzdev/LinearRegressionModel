FROM python:3.5.2
COPY ./app.py /deploy/
COPY ./index.html /deploy/
COPY ./requirements.txt /deploy/
COPY ./trained_model.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3", "app.py"]