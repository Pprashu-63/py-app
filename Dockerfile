FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 80

COPY display_aws_region.py /app/diplay_aws_region.py

CMD ["python","/app/play_aws_region.py"]