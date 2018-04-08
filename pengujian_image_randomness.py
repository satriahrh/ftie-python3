from blocks import transform
from blocks.acm import ACM
from blocks.bbs import BBS
from blocks.rt import RT
from suplementary import image_randomness as ir


def plain_and_cipher_image(bts, BBS_P, BBS_Q, BBS_S, ACM_A, ACM_B, ACM_N):
    # PREPARATION
    rt = RT(BBS(
        _p=BBS_P,
        _q=BBS_Q,
        seed=BBS_S
    ))

    acm = ACM(
        _a=ACM_A,
        _b=ACM_B,
        number_of_iteration=ACM_N
    )

    # TRANSFORMATION
    plainbytes = transform.pad_bytes(bts)

    # RANDOMIZE TEXT
    randomized_bytes = rt.encrypt(plainbytes)

    # TRANSFORMATION
    pixels = transform.compile_bytes_to_pixels(randomized_bytes)
    pixel_matrix = transform.compile_pixels_to_matrix(pixels)

    # ARNOLD'S CAT MAP
    ciphermatrix = acm.encrypt(pixel_matrix)

    # TRANSFORMATION
    return transform.matrix_to_image(pixel_matrix), \
        transform.matrix_to_image(ciphermatrix)


def pengujian(BBS_P, BBS_Q, BBS_S, ACM_A, ACM_B, ACM_N, MB):
    bts = b'1' * int(MB * 1000000)

    print(f'p\t\t: {BBS_P}')
    print(f'q\t\t: {BBS_Q}')
    print(f's\t\t: {BBS_S}')
    print(f'a\t\t: {ACM_A}')
    print(f'b\t\t: {ACM_B}')
    print(f'n\t\t: {ACM_N}')
    print(f'file\t\t: {MB}MB')

    plainimage, cipherimage = \
        plain_and_cipher_image(bts, BBS_P, BBS_Q, BBS_S, ACM_A, ACM_B, ACM_N)

    print(f'NPCR(r, g, b)\t: {ir.npcr(plainimage, cipherimage)}')
    print(f'UACI(r, g, b)\t: {ir.uaci(plainimage, cipherimage)}')
    print()


pengujian(BBS_P=99991, BBS_Q=99971, BBS_S=2, ACM_A=1, ACM_B=1, ACM_N=5, MB=1)
pengujian(BBS_P=11, BBS_Q=7, BBS_S=9, ACM_A=1, ACM_B=1, ACM_N=5, MB=1)
