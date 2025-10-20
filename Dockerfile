FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["sh", "-c", "flask --app projfold run -h 0.0.0.0 -p $PORT"]