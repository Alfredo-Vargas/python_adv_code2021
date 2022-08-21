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

bin_packet = ""
for char in packet:
    bin_packet += hex_to_bin[char]
# print(bin_packet)

def get_version_id(bin_packet):
    packet_version = bin_to_dec[bin_packet[0:3]]
    packet_id = bin_to_dec[bin_packet[3:6]]
    return (packet_version, packet_id)

print(get_version_id(bin_packet))

# if id == 4 then it is a literal_value, else it is an operator

groups = bin_packet[6:]
n_groups = len(bin_packet[6:]) // 5

literal_value = ""
for i in range(n_groups):
    group = groups[5*i:(i+1)*5]
    literal_value += group[1:]
numerical_value = int(literal_value, 2)    

