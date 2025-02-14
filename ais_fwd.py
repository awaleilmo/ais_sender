import socket
import subprocess
import threading

# Configuration: List of target (IP, Port) tuples
TARGETS = [
    ("192.168.2.135", 10110),  # Change to your first target
    ("192.168.2.187", 10110),  # Change to your second target
    ("192.168.2.127", 10110),  # Third target (if needed)
    ("192.168.2.135", 10111)   # Fourth target (if needed)
]

# Start rtl_ais and read its output
def read_rtl_ais():
    process = subprocess.Popen(["rtl_ais", "-p", "0"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    for line in iter(process.stdout.readline, ""):
        if line.strip():
            send_to_targets(line.strip())

# Send AIS data to multiple targets
def send_to_targets(message):
    for ip, port in TARGETS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (ip, port))
            sock.close()
        except Exception as e:
            print(f"Failed to send to {ip}:{port} -> {e}")

if __name__ == "__main__":
    print("Starting AIS Forwarder...")
    rtl_thread = threading.Thread(target=read_rtl_ais, daemon=True)
    rtl_thread.start()
    rtl_thread.join()  # Keep script running
