# OIBSIP_pythonprogramming_project5

# Chat Application 

## Objective
The objective of this project is to build a simple client-server chat application in Python using sockets.  
The application allows real-time communication between a client and server, supports emoji replacement, and simulates typing indicators to enhance user experience.

## Steps Performed
1. Set up the server (server.py)  
   - Created a socket to listen for incoming client connections.  
   - Accepted client connections and received their name.  
   - Displayed client messages on the server console.  
   - Allowed the server user to send responses back to the client.  

2. Developed the client (client.py)  
   - Connected to the server using sockets.  
   - Asked the user to input their name.  
   - Implemented a background thread to receive messages from the server continuously.  
   - Allowed the user to type and send messages with emoji replacement.  
   - Simulated a "Typing..." indicator before sending messages.  

3. Emoji Replacement  
   - Added a function to replace text-based emojis with Unicode emojis:  
     - :) → 😊  
     - :( → 😢  
     - :D → 😄  

4. Tested communication  
   - Launched server.py first and then client.py.  
   - Verified bidirectional communication between server and client.  
   - Confirmed emoji replacements and typing simulation worked properly.  

## Tools & Technologies Used
- Programming Language: Python 3  
- Libraries:  
  - socket (for networking)  
  - threading (to handle receiving messages concurrently)  
  - time (for typing simulation)  

## Outcome
- A fully working chat application that allows two-way communication between client and server.  
- Successfully integrated emoji replacement and typing indicators to make the chat more interactive.  
- Enhanced understanding of socket programming, multi-threading, and real-time communication in Python.  
