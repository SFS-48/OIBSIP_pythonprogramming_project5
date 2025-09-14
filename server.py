import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(1)
    print("[SERVER STARTED] Waiting for a connection...")

    client_socket, addr = server.accept()
    print(f"[CONNECTED] Client {addr} connected.")

    user_name = client_socket.recv(1024).decode()
    print(f"{user_name} has joined the chat!")

    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(f"{user_name}: {msg}")
            
            # Ask server user to type a response
            response = input("Your message: ")
            response = replace_emojis(response)
            client_socket.send(response.encode())

        except:
            print("[DISCONNECTED] Client disconnected.")
            break

    client_socket.close()
    server.close()

def replace_emojis(text):
    text = text.replace(":)", "😊")
    text = text.replace(":(", "😢")
    text = text.replace(":D", "😄")
    return text

if __name__ == "__main__":
    start_server()
