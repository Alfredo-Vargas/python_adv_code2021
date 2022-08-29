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

bin_packet = ""
for char in packet:
    bin_packet += hex_to_bin[char]

def get_version_id(bin_packet):
    packet_version = int(bin_packet[0:3], 2)
    packet_id = int(bin_packet[3:6], 2)
    return (packet_version, packet_id)

version_sum = 0
cursor_position = 0

while len(bin_packet) > 6:
    packet_version, packet_id = get_version_id(bin_packet)
    print(f"The whole binary input is: {bin_packet}")
    print(f"The version and id are: {get_version_id(bin_packet)}")
    version_sum += packet_version
    bin_packet = bin_packet[6:]  # we chop left (decapsulation)
    in_last_group = False
    if packet_id == 4:  # it is a literal
        while not in_last_group:
            group = bin_packet[0:5]
            if group[0] == '0':
                in_last_group = True
            bin_packet = bin_packet[5:]
    else:  # it is an operator
        length_type = bin_packet[0]
        if length_type == '1':
            n_subpackets = int(bin_packet[1:12], 2)
            print(f"The number of subpackets is: {n_subpackets}")
            bin_packet = bin_packet[(n_subpackets * 11 + 1):]
        else:
            n_bits_in_subpacket = int(bin_packet[1:16], 2)
            print(f"The number of n_bits in subpacket is : {n_bits_in_subpacket}")
            bin_packet = bin_packet[n_bits_in_subpacket]

print(version_sum)

# if packet_id == 4:
#     groups = bin_packet[6:]
#     n_groups = len(bin_packet[6:]) // 5
#
#     literal_value = ""
#     for i in range(n_groups):
#         group = groups[5*i:(i+1)*5]
#         literal_value += group[1:]
#     numerical_value = int(literal_value, 2)    
#     print(f"It was a literal packet with value: {numerical_value}")
# else:
#     length_type_id = 15 if bin_packet[6] == "0" else 11
#     print(f"Length type id is: {length_type_id}")
#     subpackets_length = int(bin_packet[7:7+length_type_id], 2)
#     print(f"Subpackets length type is: {subpackets_length}")
#     if subpackets_length == 1:
#         print(bin_packet[6 + 1 + length_type_id:])
#         print(get_version_id(bin_packet[6 + 1 + length_type_id:]))
