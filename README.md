
✒️**READ BEFORE RUN**

Fitness Booking API
This is a simple Django REST API project for managing fitness classes and bookings.

Project Features
GET /classes: Get a list of upcoming fitness classes.

POST /book: Book a class if slots are available.

GET /bookings?email=client_email: Get all bookings made by a specific email.

Prerequisites
Python 3.10 or higher installed on your system.

Git installed to clone the repository.

(Optional) A virtual environment tool like venv or virtualenv.

Setup Instructions
Follow these steps carefully to run the project locally:

Clone the repository:
git clone https://github.com/KIRUBAKARAN9840/omnify.git
cd omnify

Create and activate a virtual environment:

On Windows (PowerShell):
python -m venv env
.\env\Scripts\activate

On macOS/Linux:
python3 -m venv env
source env/bin/activate

Install dependencies:
pip install -r requirements.txt
(If requirements.txt is missing, run:)
pip install django djangorestframework

Apply migrations to create the database schema:
python manage.py migrate

(Optional) Create a superuser to access Django admin:
python manage.py createsuperuser
Follow prompts to create admin credentials.

Run the development server:
python manage.py runserver

Access the API and admin panel:

API endpoints:
GET http://127.0.0.1:8000/classes
POST http://127.0.0.1:8000/book
GET http://127.0.0.1:8000/bookings?email=client@example.com

Admin panel:
http://127.0.0.1:8000/admin (Login with superuser credentials)

Testing the API
Use Postman or any API client to test the endpoints.

Example: Get all classes
Method: GET
URL: http://127.0.0.1:8000/classes

Example: Book a class
Method: POST
URL: http://127.0.0.1:8000/book
Body (JSON):

json
Copy
Edit
{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
Example: Get bookings by email
Method: GET
URL: http://127.0.0.1:8000/bookings?email=john@example.com

Notes
Make sure to add classes through the Django admin panel or database before booking.

The server must be running (python manage.py runserver) to access the APIs.

If you add new models or make changes to models, run migrations again
