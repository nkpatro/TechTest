I used Django and django rest framework for this test as we have been using django tools in our production for last few years.

I haven't added any comments inline to the code. Please let me know if preferred.

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

based on what I have understood, I added a health check URL  http://localhost:8000/api/health that just gives to you a status.

I could not add anything to address the "list of files in a directory" endpoint, as the api cannot access the path beyond its root folder on the server.
To achieve this we need to mount an external drive inside our application root folder and use os.walk() to list any thing.

I have used app level versioning in this test. This is not my preferable versioning strategy, as this will have app level code duplication and url needs to be modified.
   Preferred way is to use Accept header. However, to finish the task quickly I implemented it app level.


I used the framework's builtin pagination.
    I have defaulted it to 5 entries per page. this can be modified at runtime by setting the "limit" parameter in the URL as shown below.
    http://localhost:8000/api/users/?limit=10

