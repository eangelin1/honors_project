import rsa
import socket

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