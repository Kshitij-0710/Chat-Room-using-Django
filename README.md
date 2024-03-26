<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Chat Room using Django</h1>
    <h2>Views.py:</h2>
    <ul>
        <li><strong>home(request):</strong> This function is called when someone visits the homepage of the website. It renders a template called home.html.</li>
        <li><strong>room(request, room):</strong> When someone wants to enter a chat room, this function is called. It finds the room details and renders a template called room.html with some information like the username and room details.</li>
        <li><strong>checkview(request):</strong> This function checks if a chat room exists. If it does, it redirects the user to that room. If not, it creates a new room and then redirects the user to it.</li>
        <li><strong>send(request):</strong> This function is called when someone sends a message in a chat room. It saves the message in the database and sends back a message saying it was successful.</li>
        <li><strong>getMessages(request, room):</strong> When someone wants to see the messages in a chat room, this function is called. It gets all the messages for that room from the database and sends them back as a response.</li>
    </ul>
    <h2>Running It:</h2>
    <ol>
        <li>Save the file.</li>
        <li>Make sure to have Django installed on your PC. You can install it using the following command: <code>pip install django</code></li>
        <li>In the command prompt, navigate to the path where you stored your files using: <code>cd chat</code></li>
        <li>Type the following command to start the Django server: <code>python manage.py runserver</code></li>
        <li>Open <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your web browser.</li>
        <li>Enter '404' in the room number, then choose any username you like, and press Enter. You should be able to see my message in the chat room. 
 THATS ALL!! , ALL SET</li>
    </ol>
</body>
</html>

