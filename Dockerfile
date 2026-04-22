FROM python:3.9-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Use non-root user (security best practice)
RUN useradd -m appuser
USER appuser

EXPOSE 5000

# Use production server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]