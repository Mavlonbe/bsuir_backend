FROM python:3.10.13-slim-bullseye

# Set the working directory
WORKDIR /usr/src/app

# Upgrade pip and install requirements first for better layer caching
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application
COPY . /usr/src/app/

# Set environment variable
ENV SERVICE_STATE production

# Command to run the application
CMD ["uvicorn", "notes.asgi:application", "--host", "0.0.0.0", "--port", "23335"]
