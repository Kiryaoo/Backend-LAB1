
# Backend-LAB1: Flask Application with Docker

This is a simple Flask web application packaged in a Docker container. The application has two endpoints: a main page and a healthcheck page.

## Requirements

To run this project, you will need:

- Python

- Flask

- Docker

## How to Run the Project

Clone the repository:

```
git clone [https://github.com/Kiryaoo/Backend-LAB1.git](https://github.com/Kiryaoo/Backend-LAB1.git)

```

Navigate to the project directory:

```
cd Backend-LAB1
```

Run using Docker Compose:
This command will build your Docker image and start the container.
```
docker-compose up --build
```

After completing these steps, your application will be available at http://localhost:8000.

## How to Verify

You can verify that everything is working by accessing the following endpoints in your browser or via curl.

Main Page:

- http://localhost:8000/

Expected response: 
```
Hello, World!
```
Healthcheck:

- http://localhost:8000/healthcheck

Expected response: {"status":"ok"}

## API Endpoints

- GET / - Returns a welcome message.

- GET /healthcheck - Returns a JSON object with an ok status, confirming the application is running.

## Stopping the Application

To stop the container, press Ctrl+C in the terminal where docker-compose up is running, or open a new terminal in the same directory and run:

```
docker-compose down
```
