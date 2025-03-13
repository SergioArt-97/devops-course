# Use a specific version of Python
ARG pythonVersion=3.9
FROM python:${pythonVersion}-slim

# Create a non-root user for security
RUN addgroup --system --gid 10000 appgrp \
    && adduser --home /opt/app --shell /usr/sbin/nologin --no-create-home --disabled-login --disabled-password --uid 10000 --gid 10000 app

# Set the working directory
WORKDIR /app

# Copy only the application script (No requirements.txt needed)
COPY getUser.py /app/

# Run as non-root user
USER app

# Command to run the script
CMD ["python", "getUser.py"]