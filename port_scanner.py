import socket
import sys

def scan_ports(ip, start_port, end_port):
    open_ports = []
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except socket.error:
            print(f"[-] Could not connect to port {port}")
            continue
    return open_ports

def main():
    try:
        ip = input("Enter the IP address to scan: ")
        socket.inet_aton(ip)  # Validate IP format

        start_port = int(input("Enter start port (0–65535): "))
        end_port = int(input("Enter end port (0–65535): "))

        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            print("Error: Port numbers must be between 0 and 65535.")
            sys.exit()

        if start_port > end_port:
            print("Error: Start port cannot be greater than end port.")
            sys.exit()

        open_ports = scan_ports(ip, start_port, end_port)
        if open_ports:
            print(f"\n[✓] Open ports: {open_ports}")
        else:
            print("\n[-] No open ports found.")

    except socket.error:
        print("Invalid IP address.")
    except ValueError:
        print("Please enter valid numbers for ports.")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()

if __name__ == "__main__":
    main()
