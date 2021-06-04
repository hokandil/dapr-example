FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask requests
# ADD requirements.txt .
# RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 3000
CMD ["app.py"]
