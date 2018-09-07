FROM ubuntu:latest

LABEL boydbigdatarpg "redthegx@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY . ./app
WORKDIR app/

RUN pip install -r requirements.txt
RUN pip install numpy==1.15.0
RUN pip install scikit-surprise==1.0.6

ENTRYPOINT ["python"]
CMD ["app.py"]
