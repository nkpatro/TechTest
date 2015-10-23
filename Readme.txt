I used Django and django rest framework for this as I have been using this framework for last few years.

Dependencies:
I have included a requirements.txt file to install all the dependencies.
Please run the following.

'pip install -r requirements.txt'


Deployment Instructions:
As of now this is not configured to run directly in apache server.
run the following commands to deploy:

>>> cd TechTest
>>> python manage.py runserver

testing:
run this to receive a token
>>> curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "secret!"}' http://localhost:8000/api/token-auth/

This should return a token in json:
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MSwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE0NDU2Njk2NzZ9.uffbCrFrjrh3saSXZKqybeZXntHDTl-dkFPKLFrv610"}

use the following to get all users.
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MSwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE0NDU2Njk2NzZ9.uffbCrFrjrh3saSXZKqybeZXntHDTl-dkFPKLFrv610" http://localhost:8000/api/users/


For my testing I used Postman (https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)

