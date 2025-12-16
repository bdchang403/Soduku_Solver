# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Collect static files (optional but recommended for production)
# RUN python manage.py collectstatic --noinput
# For now, we might skip or ensure static root is set. 
# Let's set a minimal static setup or just run without it if not critical for now.
# But for a real deployment, we usually need it.
# Let's assume standard behavior.

# Expose port
EXPOSE 8080

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "mysite.wsgi:application"]
