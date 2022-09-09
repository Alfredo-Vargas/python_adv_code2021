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
    elif defined_operation == "lit":
        value += next_value
    elif defined_operation == "gt":
        value = 1 if value > next_value else 0
    elif defined_operation == "lt":
        value = 1 if value < next_value else 0
    elif defined_operation == "eq":
        value = 1 if value == next_value else 0
    else:
        print(f"Non defined operation : {defined_operation}")
        return None
    return value


def get_operation(packet_id):
    def_op = ""
    start_value = 0
    if packet_id == 0:
        def_op = "sum"
    elif packet_id == 1:
        def_op = "prod"
    elif packet_id == 2:
        def_op = "min"
    elif packet_id == 3:
        def_op = "max"
    elif packet_id == 5:
        def_op = "gt"
    elif packet_id == 6:
        def_op = "lt"
    elif packet_id == 7:
        def_op = "eq"
    else:
        print(f"Non defined operation associated to id: {packet_id}")
    print(f"The operation is: {def_op}")
    return def_op


def get_string_value(bin_packet):
    in_last_group = False
    literal_value = ""
    while not in_last_group:
        group = bin_packet[0:5]
        literal_value += bin_packet[1:5]
        in_last_group = True if group[0] == "0" else False
        bin_packet = bin_packet[5:]
    value = int(literal_value, 2)
    return (value, bin_packet)


version_sum = 0


def get_value(bin_packet):
    global version_sum
    packet_version, packet_id = parse_header(bin_packet)
    version_sum += packet_version
    bin_packet = bin_packet[6:]
    if packet_id == 4:
        value, bin_packet = get_string_value(bin_packet)
        return (value, bin_packet)
    else:
        operation = get_operation(packet_id)
        length_type = 15 if bin_packet[0] == "0" else 11
        if length_type == 15:
            nbits = int(bin_packet[1:16], 2)
            bin_packet = bin_packet[16:16+nbits]
        else:
            nsubp = int(bin_packet[1:12], 2)
            bin_packet = bin_packet[12:]

        # Perform operation
        if operation == "sum":
            sum = 0
            while (len(bin_packet) > 7):
                new_term, bin_packet = get_value(bin_packet)
                sum += new_term
            return (sum, bin_packet)
        elif operation == "prod":
            prod = 1
            while (len(bin_packet) > 7):
                new_term, bin_packet = get_value(bin_packet)
                prod *= new_term
            return (prod, bin_packet)
        elif operation == "min":
            minimum = 999
            while(len(bin_packet) > 7):
                new_term, bin_packet = get_value(bin_packet)
                minimum = minimum if minimum < new_term else new_term
            return (minimum, bin_packet)
        elif operation == "max":
            maximum = 0
            while(len(bin_packet) > 7):
                new_term, bin_packet = get_value(bin_packet)
                maximum = maximum if maximum > new_term else new_term
            return (maximum, bin_packet)
        else:
            lh = int(len(bin_packet) / 2)
            lhbin = bin_packet[0:lh]
            rhbin = bin_packet[lh:]
            lhs, bin_packet = get_value(lhbin)
            rhs, bin_packet = get_value(rhbin)
            comparison = 0
            if operation == "lt":
                comparison = 1 if lhs < rhs else 0
            elif operation == "gt":
                comparison = 1 if lhs > rhs else 0
            elif operation == "eq":
                comparison = 1 if lhs == rhs else 0
            return (comparison, bin_packet)
        

# Gets answer of part 1
# print(version_sum)
# Gets answer of part 2
print(f"The result of the operation is: {get_value(bin_packet)}")
