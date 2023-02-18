
# Note App

This is a Note app built using Django and Django Rest Framework (DRF). The app allows users to create, read, update, and delete notes.It also include a login system and the ability to save notes to a remote database.

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

## Installation (local setup)

1) Clone the repository

```bash
  git clone https://github.com/<username>/note-app.git
cd note-app
```

2)Create a virtual environment and activate Installation
```bash
    python3 -m venv venv
    source venv/bin/activate
```

3) Install the dependencies
```bash
    pip install -r requirements.txt
```

4) Set up the DB
```bash
    python manage.py migrate
```

5)Start the server
```bash
  python manage.py runserver
```

6)The app should now be running at http://localhost:8000/.

To access the API endpoints, you can use a tool like curl or Postman with the appropriate URLs and headers. Alternatively, you can access the Swagger UI by following the steps below.

To access the Swagger UI, follow these steps:

Make sure the app is running locally or deployed on Fly.io.

Open a web browser and go to the URL http://localhost:8000/swagger/ if running locally, or https://late-wood-9200.fly.dev/swagger/. The Swagger UI should now be displayed, allowing you to interact with the API endpoints using a web interface.

API Endpoints
The following endpoints are available:

Notes:

GET /notes/: List all notes
POST /notes/: Create a new note
GET /notes/{id}/: Retrieve a specific note
PUT /notes/{id}/: Update a specific note
DELETE /notes/{id}/: Delete a specific note

Users:

POST /users/login/: Login a user
POST /users/register: Register a new user

Refer to the Swagger UI or the DRF documentation for more information on how to use these endpoints.


## Deployment

This app was deployed on Fly.io using their container platform. To deploy the app, follow these steps:

1)create an account on Fly.io and install the Flyctl CLI.

2)Login to Fly.io using the CLI:
```bash
  flyctl auth login
```

3)Create a new fly.io app
```bash
    flyctl apps create <app-name>
```
4) Deploy the app
```bash
    flyctl deploy
```
5) The app should now be running on Fly.io. You can access the API endpoints using the URL provided by Fly.io.

