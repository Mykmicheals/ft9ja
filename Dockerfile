FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /ft9ja

# Copy the project code to the working directory
COPY . /ft9ja/

RUN pip install --no-cache-dir celery


RUN pip install -r requirements.txt

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
