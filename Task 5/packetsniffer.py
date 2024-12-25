import scapy.all as scapy
import threading

# Global variable to control sniffing
stop_sniffing = False

def packet_analysis(packet):
    # This function processes each captured packet
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src  # Source IP address
        ip_dst = packet[scapy.IP].dst  # Destination IP address
        protocol = packet[scapy.IP].proto  # Protocol (TCP/UDP)
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")

def start_sniffing(interface=None):
    # This function starts sniffing on the specified network interface
    print("Starting packet capture...")
    # Use sniff() with stop_filter to manually control when to stop sniffing
    scapy.sniff(iface=interface, prn=packet_analysis, store=False, stop_filter=stop_sniff_condition)

def stop_sniff_condition(packet):
    # This function determines when to stop sniffing based on the global stop_sniffing flag
    return stop_sniffing  # Stop sniffing if stop_sniffing is True

def manual_stop():
    # This function waits for the user to press Enter to stop sniffing
    input("Press Enter to stop sniffing...\n")   
    global stop_sniffing
    stop_sniffing = True  # Set stop_sniffing to True to stop the sniffing

if __name__ == "__main__":
    # Get the network interface from the user
    interface = input("Enter network interface (or press Enter to use default): ").strip()
    if interface == "":
        interface = None  # Let scapy automatically detect the default interface

    # Start sniffing in a separate thread to allow manual stopping
    sniff_thread = threading.Thread(target=start_sniffing, args=(interface,))
    sniff_thread.start()

    # Wait for user input to stop sniffing
    manual_stop()
    
    # Wait for sniffing thread to finish
    sniff_thread.join()

    print("Packet sniffing stopped.")
