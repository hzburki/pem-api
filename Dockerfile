FROM python:3.10.6-slim

# Disable the output buffering, which ensures that the output of print() 
# and other standard output streams is immediately visible in the Docker 
# container logs
ENV PYTHONUNBUFFERED=1

# This is the starting directory for the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Upgrade pip to the latest version
RUN upgrade pip install --upgrade pip

# Install the requirements 
# --no-cache-dir is used to avoid caching the packages on local machine
# since docker has its own cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY ./src ./src

# This command starts the Uvicorn server to serve the FastAPI app on port 8000 
# with auto-reloading enabled. 
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]

