DATA_WIDTH = N = 4
CRC_WIDTH = M = 5

def crc5_serial(crc: int, data_in: int) -> int:
    crc_bits = [(crc >> i) & 1 for i in range(5)]

    new_crc = [0] * 5
    new_crc[0] = crc_bits[4] ^ data_in
    new_crc[1] = crc_bits[0]
    new_crc[2] = crc_bits[1] ^ crc_bits[4] ^ data_in
    new_crc[3] = crc_bits[2]
    new_crc[4] = crc_bits[3]

    return sum((bit << i) for i, bit in enumerate(new_crc))


def crc5_parallel(data_bits: list[int], initial_crc: int) -> int:
    crc = initial_crc
    for bit in data_bits:
        crc = crc5_serial(crc, bit)
    return crc


def H1():
    for x in range(DATA_WIDTH):
        data = 1 << x
        bits = [(data >> i) & 1 for i in reversed(range(8))]

        final_crc = crc5_parallel(bits, 0)
        print(f"H1 ROW Nin[{x}] = {final_crc:05b}")


def H2():
    data_bits = [0, 0, 0, 0]
    for i in range(CRC_WIDTH):
        initial_crc = 1 << i
        result_crc = crc5_parallel(data_bits, initial_crc)
        print(f"H2 ROW Min[{i}] = {result_crc:05b}")


if __name__ == "__main__":
    print("="*10)
    H1()
    print("="*10)
    H2()
    print("="*10)
