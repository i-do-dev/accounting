# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run app.py when the container launches
CMD ["sh", "-c", "python manage.py migrate && gunicorn accounting.wsgi:application --bind 0.0.0.0:8000"]
