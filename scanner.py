
output_file = open("scan_results.txt","w")

print("""
===================================
      PYTHON NETWORK SCANNER
      Cybersecurity Project
===================================
""")

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS"
}


import socket
from threading import Thread

target = input("Enter target (IP or website): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning target: {target}\n")

def scan_port(port):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:

        service = services.get(port, "Unknown")

        message = f"Port {port} OPEN ({service})"

        print(message)
        output_file.write(message + "\n")

    scanner.close()

threads = []

for port in range(start_port, end_port + 1):

    thread = Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

output_file.close()


