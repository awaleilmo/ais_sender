import socket
import time

# ✅ Configure the target IP and UDP port
# TARGET_IP = "192.168.2.187"  # Change to target IP
TARGET_IP = "127.0.0.1"  # Change to target IP
TARGET_PORT = 10110          # Change to target UDP port

# ✅ Function to load AIS messages from a CSV file
def load_ais_messages_from_csv(file_path):
    messages = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                message = line.strip()  # Remove leading/trailing whitespaces
                if message:  # Skip empty lines
                    messages.append(message)
        return messages
    except FileNotFoundError:
        print(f"⚠️ File '{file_path}' not found. Please check the path.")
        return []
    except Exception as e:
        print(f"⚠️ An error occurred while reading the file: {e}")
        return []

# ✅ Path to AIS messages CSV file
AIS_CSV_FILE = "nmea_merak.csv"

# ✅ Load AIS messages from the CSV file
AIS_MESSAGES = load_ais_messages_from_csv(AIS_CSV_FILE)

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
