from registration.creator_registration import generate_code,register_with_code
from discovery.discovery_server import start_discovery
from scanner.agent_scanner import scan_for_agents
from communication.agent_network import send_message
from protocol.ai_civilization_protocol_v1 import show_protocol

def menu():

    while True:

        print("\nAI Civilization Control")

        print("1 Generate Creator Code")
        print("2 Register Agent")
        print("3 Start Discovery")
        print("4 Scan AI Agents")
        print("5 Send Message")
        print("6 Show Protocol")
        print("7 Exit")

        c=input("Select:")

        if c=="1":
            generate_code()

        elif c=="2":
            register_with_code()

        elif c=="3":
            start_discovery()

        elif c=="4":
            scan_for_agents()

        elif c=="5":

            s=input("Sender:")
            r=input("Receiver:")
            m=input("Message:")

            send_message(s,r,m)

        elif c=="6":
            show_protocol()

        elif c=="7":
            break

print("Governor AI Started")

menu()
