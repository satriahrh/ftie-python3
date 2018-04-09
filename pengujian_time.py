from blocks import acm, bbs, rt, transform
from os import path
from time import time


class Timer:
    def __init__(self):
        self.__last_checkpoint = time()

    def checkpoint(self):
        ret = time() - self.__last_checkpoint
        self.__last_checkpoint = time()
        return ret


class ApplicationTime:
    def __init__(
        self,
        bbs_p, bbs_q, bbs_seed,
        acm_a, acm_b, acm_n,
    ):
        # BBS
        self.__bbs = bbs.BBS(_p=bbs_p, _q=bbs_q, seed=bbs_seed)

        # RT
        self.__rt = rt.RT(self.__bbs)

        # ACM
        self.__acm = acm.ACM(_a=acm_a, _b=acm_b, number_of_iteration=acm_n)

    def encrypt(self, plainfile_filepath, cipherimage_filepath=None):

        ret = {}

        timer = Timer()

        # PREPARATION
        if cipherimage_filepath is not None:
            if cipherimage_filepath[-3:].lower() != "bmp":
                cipherimage_filepath += ".bmp"
        else:
            cipherimage_filepath = plainfile_filepath + ".bmp"

        # TRANSFORMATION
        bts = transform.file_to_bytes(plainfile_filepath)

        ret['transform.file_to_bytes'] = timer.checkpoint()

        plainbytes = transform.pad_bytes(bts)

        ret['transform.pad_bytes'] = timer.checkpoint()

        # RANDOMIZE TEXT
        randomized_bytes = self.__rt.encrypt(plainbytes)

        ret['RT.encrypt'] = timer.checkpoint()

        # TRANSFORMATION
        pixels = transform.compile_bytes_to_pixels(randomized_bytes)

        ret['transform.compile_bytes_to_pixels'] = timer.checkpoint()

        pixel_matrix = transform.compile_pixels_to_matrix(pixels)

        ret['transform.compile_pixels_to_matrix'] = timer.checkpoint()

        # ARNOLD'S CAT MAP
        ciphermatrix = self.__acm.encrypt(pixel_matrix)

        ret['ACM.encrypt'] = timer.checkpoint()

        # TRANSFORMATION
        cipherimage = transform.matrix_to_image(ciphermatrix)

        ret['transform.matrix_to_image'] = timer.checkpoint()

        # CIPHERIMAGE SAVING
        cipherimage.save(cipherimage_filepath)

        ret['Image.save'] = timer.checkpoint()

        return ret

    def decrypt(self, cipherimage_filepath, plainfile_filepath):
        from PIL import Image

        ret = {}

        timer = Timer()

        # OPEN IMAGE
        cipherimage = Image.open(cipherimage_filepath, mode='r')

        ret['Image.open'] = timer.checkpoint()

        # TRANSFORMATION
        ciphermatrix = transform.image_to_matrix(cipherimage)

        ret['transform.image_to_matrix'] = timer.checkpoint()

        # ARNOLD'S CAT MAP
        pixel_matrix = self.__acm.decrypt(ciphermatrix)

        ret['ACM.decrypt'] = timer.checkpoint()

        # TRANSFORMATION
        pixels = transform.decompile_matrix_to_pixels(pixel_matrix)

        ret['transform.decompile_matrix_to_pixels'] = timer.checkpoint()

        randomized_bytes = transform.decompile_pixels_to_bytes(pixels)

        ret['transform.decompile_pixels_to_bytes'] = timer.checkpoint()

        # DERANDOMIZED TEXT
        plainbytes = self.__rt.decrypt(randomized_bytes)

        ret['RT.decrypt'] = timer.checkpoint()

        # TRANSFORMATION
        bts = transform.strip_bytes(plainbytes)

        ret['transform.strip_bytes'] = timer.checkpoint()

        transform.bytes_to_file(bts, plainfile_filepath)

        ret['transform.bytes_to_file'] = timer.checkpoint()

        return ret


def pengujian(P, Q, S, A, B, N, MB):
    pengujian_id = f'{MB}_{P}_{Q}_{S}_{A}_{B}_{N}'

    print(f'ID {pengujian_id}')

    plainfile_filepath = path.join(
        'build', 'time',
        pengujian_id
    )
    fstream = open(plainfile_filepath, 'wb')
    fstream.write(b'1' * int(MB * 1000000))
    fstream.close()

    encr = ApplicationTime(P, Q, S, A, B, N).encrypt(
        plainfile_filepath, plainfile_filepath + '.bmp'
    )
    encr_total = sum(encr.values())

    decr = ApplicationTime(P, Q, S, A, B, N).decrypt(
        plainfile_filepath + '.bmp', plainfile_filepath
    )
    decr_total = sum(decr.values())


    print('ENCRYPTION')
    for key in encr:
        key_time = encr[key]
        persen = key_time / encr_total * 100
        print('{:40} {:15.10f}s {:5.3f}%'.format(key, key_time, persen))

    print()

    print('DECRYPTION')
    for key in decr:
        key_time = decr[key]
        persen = key_time / decr_total * 100
        print('{:40} {:15.10f}s {:5.3f}%'.format(key, key_time, persen))

    print()


if __name__ == '__main__':
    MB = 0.001

    P, Q, S, A, B, N = 11, 7, 9, 1, 1, 2
    pengujian(P, Q, S, A, B, N, MB)
