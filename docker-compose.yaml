# Use the official Python image
FROM python:3.9-alpine as python_base

# Install dependencies and build the Python app
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY app.py .

# Set up Nginx
FROM nginx:alpine as nginx_base

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the Flask app from the Python container
COPY --from=python_base /app /app

# Expose ports for Nginx (80) and Flask (8000 for Gunicorn)
EXPOSE 80
EXPOSE 8000

# Run Gunicorn for the Flask app in the background
CMD ["sh", "-c", "gunicorn --workers 3 --bind 0.0.0.0:8000 app:app & nginx -g 'daemon off;'"]