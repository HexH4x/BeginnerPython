import sys
import socket
from datetime import datetime
import threading

# Function to scan a port on the target host
def scan_port(target,port):
    try:
        # Create a TCP socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Set a timeout for the connection attempt

        # Attempt to connect to the port on the target host
        result = s.connect_ex((target,port)) # Returns 0 if the port is open

        if result == 0:
            print(f"Port {port} is open") # Port is open and accepting connections
        s.close() # Close the socket after each attempt

    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")

# Main function: validates arguments, resolves target, and initiates scan
def main():
    # Check if user provided exactly one argument (the target hostname/IP)
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments.")
        print("Usage: python.exe scanner.py <target>")
        sys.exit(1)

    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Add a pretty banner
    print("-" *50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        # Use multithreading to loop through all 65,535 ports
        threads = []
        for port in range (1,65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)

    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nScan completed!")

# Start the program
if __name__ == "__main__":
    main()
