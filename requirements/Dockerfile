FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.md .

# Install the Python libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.md

# Copy the rest of your project files to the container
COPY . .

# Specify the command to run your Python script
CMD ["python", "main.py"]