FROM python:3.11-slim

#set environmrnt variables 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work directory 
WORKDIR /app

#Install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy project
COPY . .

#run the application
CMD ["gunicorn", "school.wsgi:application", "--bind", "0.0.0.0:8000"]

