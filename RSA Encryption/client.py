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

'''
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

bob_priv = rsa.PrivateKey.load_pkcs1('PEM')

message = server_listen()
uMess = rsa.decrypt(message, bob_priv)

dMess = uMess.decode('utf8')

print(dMess)
'''