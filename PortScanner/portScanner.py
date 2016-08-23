import sys
from socket import *

host = sys.argv[1]
portList = sys.argv[2].split("-")


start = int(portList[0])
end = int(portList[1])


target_ip = gethostbyname(host)
ports = []

for port in range(start, end):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        ports.append(port)

print("Opened ports:")

for port in ports:
    print(port)
