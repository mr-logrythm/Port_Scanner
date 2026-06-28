import socket

target = input('Target (IP / Hostname): ')
if target.isalpha():
    target = socket.gethostbyname(target)
start_port = int(input("Start scan at port: "))
end_port = int(input("End scan at port: "))
open_ports = []

i = start_port
while i >= start_port and i <= end_port:
    HOST = target
    PORT = i
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner_socket.settimeout(3)
    scan_result = scanner_socket.connect_ex((HOST, PORT))
    if scan_result == 0:
        print(f'Port {PORT}: OPEN')
        open_ports.append(PORT)
    else:
        print(f'Port {PORT}: CLOSED')
    scanner_socket.close()
    i += 1

print("Scan Complete!")
if len(open_ports) > 0:
    print("Open Ports:")
    for port in open_ports:
        print(port)
else:
    print("No open port was found!")