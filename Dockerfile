# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#env path to find exicutable
ENV PATH="/animeta/:/venv/Scripts:${PATH}"

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Command to run FastAPI application
CMD ["uvicorn", "animatediff.api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
