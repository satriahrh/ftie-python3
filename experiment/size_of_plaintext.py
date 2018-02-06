# this mini experiment is used to calculate size of plaintext

def count_plaintext_byte_maximum_by_N(N):
    return N ** 2 * 3 / 2

def count_plaintext_byte_maximum_by_size(max_file_size):
    N = 2
    size = count_plaintext_byte_maximum_by_N(N)
    while size <= max_file_size:
        new_N = N + 2
        new_size = count_plaintext_byte_maximum_by_N(new_N)
        print(new_N, new_size)
        N = new_N
        size = new_size
    else:
        print('The result is N={}, for |P|={}'.format(N, int(size)))
        return N, int(size)


if __name__ == "__main__":
    max_file_size = 26214400
    N, size = count_plaintext_byte_maximum_by_size(max_file_size)  # in byte = 25 MB
    print('difference {}'.format(abs(size-max_file_size)))
