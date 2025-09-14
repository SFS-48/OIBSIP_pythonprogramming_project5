import socket
import threading
import time

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    name = input("Enter your name: ")
    client.send(name.encode())

    def receive_messages():
        while True:
            try:
                msg = client.recv(1024).decode()
                if msg:
                    print("\nServer: " + msg)
            except:
                print("[ERROR] Disconnected from server.")
                client.close()
                break

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        message = input(f"{name}: ")
        message = replace_emojis(message)
        print("Typing...")
        time.sleep(0.3)  # Typing indicator simulation
        client.send(message.encode())

def replace_emojis(text):
    text = text.replace(":)", "😊")
    text = text.replace(":(", "😢")
    text = text.replace(":D", "😄")
    return text

if __name__ == "__main__":
    start_client()
