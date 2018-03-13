from app import Application
from memory_profiler import memory_usage
from time import time

def pengujian_encrypt(p, q, s, a, b, n, mb):
    print('==========================')
    print(f'p\t\t: {p}')
    print(f'q\t\t: {q}')
    print(f's\t\t: {s}')
    print(f'a\t\t: {a}')
    print(f'b\t\t: {b}')
    print(f'n\t\t: {n}')
    print(f'file\t\t: {mb}MB')
    fstream = open('pengujian', 'wb')
    fstream.write(bytes(1000000 * mb))
    fstream.close()
    start = time()
    memory = memory_usage(
        (encrypt, (p, q, s, a, b, n)),
        interval=0.2
    )
    time_consumed = time() - start
    print(f'time_consumed\t: {time_consumed}s')
    print(f'memory usage\t: {memory}')


def encrypt(p, q, s, a, b, n):
    Application(p, q, s, a, b, n).encrypt('pengujian', 'pengujian')


if __name__ == '__main__':
    print('PENGUJIAN ACM DISCRETE')
    for i in range(1, 21):
        pengujian_encrypt(11, 7, 9, 1, 1, 1, i)

    print('PENGUJIAN ACM GENERAL EQUAL')
    for i in range(1, 21):
        pengujian_encrypt(11, 7, 9, 2, 2, 1, i)
