import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "16.in"

packet = [hex for hex in open(infile).readline().rstrip()]

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

bin_to_dec = {"100": 4, "110": 6}


def get_version_id(packet):
    first_nibble = hex_to_bin[packet[0]]
    second_nibble = hex_to_bin[packet[1]]
    packet_version = bin_to_dec[first_nibble[0:3]]
    packet_id = bin_to_dec[first_nibble[-1] + second_nibble[0:2]]
    return (packet_version, packet_id)

def get_next_group(packet, position):

second_nibble = hex_to_bin[packet[1]]
third_nibble = hex_to_bin[packet[2]]
group = next_five
while (group[0] == "1")
