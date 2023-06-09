# Use the official tensorflow image
FROM tensorflow/tensorflow:latest

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Set the working directory to /app
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy the current directory contents into the container at /app
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
# EXPOSE 8080 # not needed for Cloud Run

# Run the app when the container launches
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app