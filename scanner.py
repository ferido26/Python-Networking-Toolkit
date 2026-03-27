import socket

# Target to scan
target = input("Enter target IP: ")

# Port range
start_port = 20
end_port = 100

print(f"\nScanning target: {target}")
print("-" * 40)

for port in range(start_port, end_port + 1):
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 1 second timeout

        # Try connecting
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")

        s.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")