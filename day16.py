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

# We parse from hex to binary
bin_packet = ""
for char in packet:
    bin_packet += hex_to_bin[char]


def parse_header(bin_packet):
    packet_version = int(bin_packet[0:3], 2)
    packet_id = int(bin_packet[3:6], 2)
    return (packet_version, packet_id)




def operate(defined_operation, value, next_value):
    if defined_operation == "sum":
        value += next_value
    elif defined_operation == "prod":
        value *= next_value
    elif defined_operation == "min":
        value = next_value if value > next_value else value
    elif defined_operation == "max":
        value = next_value if value < next_value else value
    elif defined_operation == "gt":
        value = 1 if value > next_value else 0
    elif defined_operation == "lt":
        value = 1 if value < next_value else 0
    elif defined_operation == "eq":
        value = 1 if value == next_value else 0
    else:
        print(f"Non defined operation : {defined_operation}")
    return value

def get_operation(packet_id):
    def_op = ""
    start_value = 0
    if packet_id == 0:
        def_op = "sum"
        start_value = 0
    elif packet_id == 1:
        def_op = "prod"
        start_value = 1
    elif packet_id == 2:
        def_op = "min"
        start_value = 999
    elif packet_id == 3:
        def_op = "max"
        start_value = 0
    elif packet_id == 5:
        def_op = "gt"
        start_value = 0
    elif packet_id == 6:
        def_op = "lt"
        start_value = 999
    elif packet_id == 7:
        def_op = "eq"
        start_value = 0
    else:
        print(f"Non defined operation associated to id: {packet_id}")
    print(f"The operation is: {def_op}")
    return (def_op, start_value)


def get_value(bin_packet):
    version_sum = 0
    fr = 0  # final_result
    # While there is more than a header plus a prefix which is always present
    while len(bin_packet) > 7:
        packet_version, packet_id = parse_header(bin_packet)
        print(f"The whole binary input is: {bin_packet}")
        print(f"The version and id are: {packet_version, packet_id}")
        version_sum += packet_version
        # we chop left (decapsulation)
        bin_packet = bin_packet[6:]
        # get defined operation and start value
        defined_operation, fr = get_operation(bin_packet)

        if packet_id == 4:  # it is a literal
            in_last_group = False  # used for literal values
            literal_string = ""
            while not in_last_group:
                group = bin_packet[0:5]
                literal_string += bin_packet[1:5]
                if group[0] == "0":
                    in_last_group = True
                bin_packet = bin_packet[5:]  # we chop 5 bits left
            fr = int(literal_string, 2)
        else:  # it is an operator
            length_type = bin_packet[0]
            if length_type == "0":
                n_bits_in_subpacket = int(bin_packet[1:16], 2)
                print(f"Number of bits in subpacket is : {n_bits_in_subpacket}")
                bin_packet = bin_packet[16:16+n_bits_in_subpacket]
                fr = get_value(bin_packet)
                # fr = operate(defined_operation, fr, bin_packet)
            else:
                n_subpackets = int(bin_packet[1:12], 2)
                print(f"The number of subpackets is: {n_subpackets}")
                bin_packet = bin_packet[12:]
    return fr

# Gets answer of part 1
# print(version_sum)
# Gets answer of part 2
print(f"The result of the operation is: {get_value(bin_packet)}")
