#import rsa
import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # Each step will send this amount

HOST = '192.168.0.39'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
filename = "SEND/data.txt" # The file to send
print(filename)
filesize = os.path.getsize(filename) # The size of the file to send

# Connecting to host with port
s = socket.socket()
print(f"[+] Connecting to {HOST}:{PORT}")
s.connect((HOST, PORT))
print("[+] Connected.")

# Sending filename and size
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# Sending file itself
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # then sending is complete
            break
        # we use sendall to assure transmission in busy networks
        s.sendall(bytes_read)
        # update progress bar
        progress.update(len(bytes_read))

# Close socket
s.close()

