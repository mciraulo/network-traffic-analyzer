from scapy.all import sniff, IP, TCP, UDP, ICMP

def capture(packet):
    print(packet.summary())

sniff(prn=capture, count=10)