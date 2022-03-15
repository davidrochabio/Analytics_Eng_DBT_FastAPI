FROM python:3.8
ADD /api /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 8000