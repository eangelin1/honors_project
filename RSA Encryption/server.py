#import rsa
import socket
import tqdm
import os

# Device IP Address
SERVER_HOST = "192.168.0.39"
SERVER_PORT = 65432

# Receive 4096 bytes each step
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Create server socket
# TCP socket
s = socket.socket()

# Bind socket to local address
s.bind((SERVER_HOST, SERVER_PORT))

# Enable server to accept connections
# 5 here is the number of unaccepted connections
# that the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# Accept connection if there is any
client_socket, address = s.accept()

# If below code is executed, that means the sender is connected
print(f"[+] {address} is connected")

# Recieve file info
# Recieve using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

# Remove absolute path if there is one
filename = "RECEIVE/"+os.path.basename(filename)
# Convert to integer
filesize = int(filesize)

# Start receiving file from the socket and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # Nothing is recieved
            # File transmission done
            break
        # Write to file the bytes just received
        f.write(bytes_read)
        # Update progress bar
        progress.update(len(bytes_read))

# close client socket
client_socket.close()
# close server socket
s.close()

'''
message = input("What do you wanna say to Bob: ")

HOST = '127.0.0.1' # localhost
PORT = 65432 # non-priviledged ports > 1023

def server_listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print("received data...")
                if not data or data=='':
                    print("NO DATA")
                    break
                else:
                    print("sending data...")
                    print(data)
                    conn.sendall(data)
                    return data

data = server_listen()
message = data.decode('utf8')

bob_pub = rsa.PublicKey.load_pkcs1('PEM')

crypto = rsa.encrypt(message, bob_pub)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(crypto)
    data = s.recv(1024)
'''