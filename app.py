from blocks import acm, bbs, rt, transform
from time import time


# TODO: REVERT THIS COMMIT
class Application:
    def __init__(
        self,
        bbs_p, bbs_q, bbs_seed,
        acm_a, acm_b, acm_n,
    ):
        # RT
        self.__rt = rt.RT(bbs_p=bbs_p, bbs_q=bbs_q, bbs_seed=bbs_seed)

        # ACM
        self.__acm = acm.ACM(_a=acm_a, _b=acm_b, number_of_iteration=acm_n)

    def encrypt(self, plainfile_filepath, cipherimage_filepath=None):

        # PREPARATION
        print('PREPARATION')
        start = time()
        if cipherimage_filepath is not None:
            if cipherimage_filepath[-3:].lower() != "bmp":
                cipherimage_filepath += ".bmp"
        else:
            cipherimage_filepath = plainfile_filepath + ".bmp"
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        bts = transform.file_to_bytes(plainfile_filepath)
        plainbytes = transform.pad_bytes(bts)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # RANDOMIZE TEXT
        print('RANDOMIZE')
        start = time()
        randomized_bytes = self.__rt.encrypt(plainbytes)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        pixels = transform.compile_bytes_to_pixels(randomized_bytes)
        pixel_matrix = transform.compile_pixels_to_matrix(pixels)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # ARNOLD'S CAT MAP
        print('ACM')
        start = time()
        ciphermatrix = self.__acm.encrypt(pixel_matrix)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        cipherimage = transform.matrix_to_image(ciphermatrix)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # CIPHERIMAGE SAVING
        print('SAVING')
        start = time()
        cipherimage.save(cipherimage_filepath)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

    def decrypt(self, cipherimage_filepath, plainfile_filepath):
        from PIL import Image

        cipherimage = Image.open(cipherimage_filepath, mode='r')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        ciphermatrix = transform.image_to_matrix(cipherimage)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # ARNOLD'S CAT MAP
        print('ACM')
        start = time()
        pixel_matrix = self.__acm.decrypt(ciphermatrix)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        pixels = transform.decompile_matrix_to_pixels(pixel_matrix)
        randomized_bytes = transform.decompile_pixels_to_bytes(pixels)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # DERANDOMIZED TEXT
        print('RANDOMIZE')
        start = time()
        plainbytes = self.__rt.decrypt(randomized_bytes)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')

        # TRANSFORMATION
        print('TRANSFORMATION')
        start = time()
        bts = transform.strip_bytes(plainbytes)
        transform.bytes_to_file(bts, plainfile_filepath)
        print(f'Time elapsed {time() - start:{20}.{15}f}\n')
