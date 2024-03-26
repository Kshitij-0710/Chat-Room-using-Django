# Chat-Room-using-Django

VIEWS.PY:

home(request): This function is called when someone visits the homepage of the website. It renders a template called home.html.
room(request, room): When someone wants to enter a chat room, this function is called. It finds the room details and renders a template called room.html with some information like the username and room details.
checkview(request): This function checks if a chat room exists. If it does, it redirects the user to that room. If not, it creates a new room and then redirects the user to it.
send(request): This function is called when someone sends a message in a chat room. It saves the message in the database and sends back a message saying it was successful.
getMessages(request, room): When someone wants to see the messages in a chat room, this function is called. It gets all the messages for that room from the database and sends them back as a response.

for detailed explanation contact me.

RUNNING IT:
STEP 1: SAVE THE FILE
STEP 2: MAKE SURE TO HAVE DJANGO INSTALLED ON YOUR PC (pip install django) 
STEP 3: IN COMMAND PROMPT REDIRECT TO THE PATH WHERE YOU STORED YOUR FILES IN THEN [cd chat]
STEP 4: TYPE THIS [python manage.py runserver]
STEP 5: OPEN http://127.0.0.1:8000
STEP 6: ENTER '404' IN THE ROOM NUMBER THEN ANY USERNAME U LIKE PRESS ENTER AND YOURE ALL SET IF YOU CAN SEE MY MESSAGE
