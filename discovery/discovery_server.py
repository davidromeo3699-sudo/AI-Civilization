import socket

def start_discovery():

    host="0.0.0.0"
    port=9000

    s=socket.socket()

    s.bind((host,port))

    s.listen(5)

    print("Discovery Server Running on port",port)

    while True:

        conn,addr=s.accept()

        print("Agent Connected:",addr)

        conn.send(b"AI Civilization Discovery Node")

        conn.close()
