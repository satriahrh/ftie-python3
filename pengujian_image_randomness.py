from blocks import transform
from blocks.acm import ACM
from blocks.bbs import BBS
from blocks.rt import RT
from suplementary import image_randomness as ir


def plain_and_cipher_image(bts, P, Q, S, A, B, N):
    # PREPARATION
    rt = RT(BBS(
        _p=P,
        _q=Q,
        seed=S
    ))

    acm = ACM(
        _a=A,
        _b=B,
        number_of_iteration=N
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


def pengujian(P, Q, S, A, B, N, MB):
    pengujian_id = f'{MB}_{P}_{Q}_{S}_{A}_{B}_{N}'

    print(f'ID {pengujian_id}')

    bts = b'1' * int(MB * 1000000)

    plainimage, cipherimage = \
        plain_and_cipher_image(bts, P, Q, S, A, B, N)

    print(f'NPCR(r, g, b)\t: {ir.npcr(plainimage, cipherimage)}')
    print(f'UACI(r, g, b)\t: {ir.uaci(plainimage, cipherimage)}')
    print()


if __name__ == '__main__':
    MB = 0.001

    P, Q, S, A, B, N = 11, 7, 9, 1, 1, 5
    pengujian(P, Q, S, A, B, N, MB)

    P, Q, S, A, B, N = 99991, 99971, 2, 1, 1, 5
    pengujian(P, Q, S, A, B, N, MB)
