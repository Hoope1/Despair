FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt
COPY . .
ENTRYPOINT ["python", "-m"]
CMD ["main"]
