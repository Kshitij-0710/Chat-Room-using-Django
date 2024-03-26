#Chat Application Using Django
This Django project implements a simple chat application where users can enter chat rooms, send messages, and view messages in real-time.

Views
home(request): Renders the homepage template (home.html).
room(request, room): Renders the chat room template (room.html) with details about the room and the current user.
checkview(request): Checks if a chat room exists. If not, it creates a new room and redirects the user to it.
send(request): Handles sending messages in a chat room by saving the message in the database and sending a success response.
getMessages(request, room): Retrieves messages for a chat room from the database and sends them as a response.
Running the Application
Save the files.
Ensure Django is installed on your PC (pip install django).
Open a command prompt and navigate to the directory where the files are stored (cd chat).
Run the Django development server by executing python manage.py runserver.
Open http://127.0.0.1:8000 in your web browser.
Enter '404' as the room number, choose a username, and press enter to join the chat room.
You should now be able to see and send messages in the chat room.
