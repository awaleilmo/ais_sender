import socket
import time

# ✅ Configure the target IP and UDP port
TARGET_IP = "192.168.2.187"  # Change to target IP
# TARGET_IP = "127.0.0.1"  # Change to target IP
TARGET_PORT = 10110          # Change to target UDP port

# ✅ Function to read AIS messages from a file
def load_ais_messages(file_path):
    try:
        with open(file_path, "r") as file:
            messages = [line.strip() for line in file if line.strip()]
        return messages
    except FileNotFoundError:
        print(f"⚠️ File '{file_path}' not found. Please check the path.")
        return []
    except Exception as e:
        print(f"⚠️ An error occurred while reading the file: {e}")
        return []

# ✅ Path to AIS messages file
AIS_MESSAGES_FILE = "nmea_polair.txt"

# ✅ Load AIS messages from the file
AIS_MESSAGES = load_ais_messages(AIS_MESSAGES_FILE)

if not AIS_MESSAGES:
    print("⚠️ No AIS messages to send. Exiting...")
else:
    # ✅ Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            for message in AIS_MESSAGES:
                print(f"📡 Sending: {message}")
                sock.sendto(message.encode(), (TARGET_IP, TARGET_PORT))
                time.sleep(1)  # Adjust interval if needed

    except KeyboardInterrupt:
        print("\n⚠️ Simulation stopped by user.")

    finally:
        sock.close()
