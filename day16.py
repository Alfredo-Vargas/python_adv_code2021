# Original solution taken from:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/16.py
# Here are my added comments to go by

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "16.in"
data = open(infile).read().strip()
# int(data, 16) returns the decimal value of data which was given in base 16
# bin(...) converts to binary with prefix 0b will not pad correctly the zeros
binary = bin(int(data, 16))[2:]

# correction to the padding in case there are missing zeros to the left
while len(binary) < 4 * len(data):
    binary = "0" + binary
assert len(binary) % 4 == 0
assert len(binary) == 4 * len(data)

version_sum = 0


def parse(bits, i, indent):
    """Takes the bitstream, a start index, and the depth of the packet.
    Return (eval of packet, next bit after this packet)
    """
    # bits[a:b] means [a,b), so the next interval is [b,...)
    global version_sum
    version = int(bits[i+0:i+3], 2)
    version_sum += version
    type_ = int(bits[i+3:i+6], 2)
    if type_ == 4:  # lit
        i += 6  # we move the pointer to skip header
        v = 0
        while True:
            # each group of 4 corresponds to 1 digit in hexadecimal
            # so shifting one digit is the same as multiplying by 16!!!
            v = v * 16 + int(bits[i+1:i+5], 2)
            i += 5
            if bits[i-5] == "0":  # meaning last group
                return v, i
    else:
        len_id = int(bits[i+6], 2)  # get the length type
        vs = []
        if len_id == 0:  # length type is 15
            # length of bits in the sub-packet
            len_bits = int(bits[i+7:i+7+15], 2)
            # print(f'len_bits={len_bits} {bits[i+7:i+7+15]}')
            start_i = i + 7 + 15
            i = start_i
            while True:
                # get the next parse value
                v, next_i = parse(bits, i, indent + 1)
                vs.append(v)
                i = next_i  # move the pointer to the next position
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[i+7:i+7+11], 2)  # length type is 11
            i += 7 + 11  # update pointer position
            for _ in range(n_packets):
                v, next_i = parse(bits, i, indent + 1)
                vs.append(v)
                i = next_i
        if type_ == 0:
            return sum(vs), i
        elif type_ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type_ == 2:
            return min(vs), i
        elif type_ == 3:
            return max(vs), i
        elif type_ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type_ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type_ == 7:
            return (1 if vs[0] == vs[1] else 0), i
        else:
            assert False, type_


value, next_i = parse(binary, 0, 0)
print(version_sum)
print(value)
