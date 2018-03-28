from app import Application
from memory_profiler import memory_usage
from time import time


def pengujian(p, q, s, a, b, n, mb, fungsi):
    print('==========================')
    fstream = open('pengujian'+str(mb), 'wb')
    fstream.write(b'1' * mb * 1000000)
    fstream.close()
    start = time()
    memory = memory_usage(
        (fungsi, (p, q, s, a, b, n, mb)),
        interval=1
    )
    time_consumed = time() - start
    print(f'p\t\t: {p}')
    print(f'q\t\t: {q}')
    print(f's\t\t: {s}')
    print(f'a\t\t: {a}')
    print(f'b\t\t: {b}')
    print(f'n\t\t: {n}')
    print(f'file\t\t: {mb}MB')
    print(f'time_consumed\t: {time_consumed}s')
    print(f'memory usage\t: {memory}')


def encrypt(p, q, s, a, b, n, mb):
    plainfile_fp = 'pengujian'+str(mb)
    cipherimage_fp = 'pengujian'+str(mb)
    Application(p, q, s, a, b, n).encrypt(plainfile_fp, cipherimage_fp)


def decrypt(p, q, s, a, b, n, mb):
    cipherimage_fp = 'pengujian'+str(mb)+'.bmp'
    plainfile_fp = 'pengujian'+str(mb)
    Application(p, q, s, a, b, n).decrypt(cipherimage_fp, plainfile_fp)


if __name__ == '__main__':
    print('PENGUJIAN ACM DISCRETE ==========================')
    print('ENKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 1, 1, 100, i, encrypt)

    print()

    print('DEKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 1, 1, 100, i, decrypt)

    print()
    print()

    print('PENGUJIAN ACM GENERAL a = b =====================')
    print('ENKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 2, 2, 100, i, encrypt)

    print()

    print('DEKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 2, 2, 100, i, decrypt)

    print('PENGUJIAN ACM GENERAL any a and b ===============')
    print('ENKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 3, 4, 100, i, encrypt)

    print()

    print('DEKRIPSI ========================================')
    for i in range(1, 21):
        pengujian(11, 7, 9, 3, 4, 100, i, decrypt)
