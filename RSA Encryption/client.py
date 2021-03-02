import rsa
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

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

