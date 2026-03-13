import socket

def scan_for_agents():

    print("Scanning network for AI agents...")

    for i in range(1,255):

        ip=f"192.168.1.{i}"

        try:

            s=socket.socket()

            s.settimeout(0.3)

            s.connect((ip,9000))

            print("Agent Found:",ip)

            s.close()

        except:
            pass
