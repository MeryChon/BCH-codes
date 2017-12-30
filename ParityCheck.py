import sys

import Polynomial


def parse_input_file(input_file):
    file_obj = open(input_file, 'r')
    raw_data = file_obj.read().split()
    return int(raw_data[0]), int(raw_data[1]), [int(i) for i in raw_data[2:]]


def reverse(pol):
    res = []
    for i in range(len(pol)-1, -1, -1):
        res.append(pol[i])
    return res


def write_to_file(output_file, result, pwr):
    file_obj = open(output_file, 'w')
    to_write = ""
    if result[0]:
        to_write += "YES\n"
        pol_to_write = reverse(result[1])
        zeroes = [0 for i in range(pwr - len(pol_to_write))]
        pol_to_write = reverse(result[1]) + zeroes
        for i in pol_to_write:
            to_write += str(i) + " "
    else:
        to_write = "NO"
    file_obj.write(to_write.strip() + "\n")
    file_obj.close()


if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    p, power, polynomial = parse_input_file(in_file)
    reversed_polynomial = reverse(polynomial)
    res = Polynomial.is_generator_polynomial(reversed_polynomial, power, p)
    write_to_file(out_file, res, power)
