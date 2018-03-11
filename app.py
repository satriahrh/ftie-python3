from blocks import acm, bbs, rt, transform
import os


class Application:
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

        # PREPARATION
        if cipherimage_filepath is not None:
            if cipherimage_filepath[-3:].lower() != "bmp":
                cipherimage_filepath += ".bmp"
        else:
            cipherimage_filepath = plainfile_filepath + ".bmp"

        # TRANSFORMATION
        list_of_byte = transform.file_to_bytes(plainfile_filepath)
        print(len(list_of_byte))

        # RANDOMIZE TEXT
        randomized_byte = self.__rt.encrypt(list_of_byte)
        print(len(randomized_byte))

        # TRANSFORMATION
        list_of_pixel = transform.numbers_to_pixels(randomized_byte)
        print(len(list_of_pixel))
        matrix_of_pixel = transform.pixels_to_matrix(list_of_pixel)
        print(len(matrix_of_pixel))

        # ARNOLD'S CAT MAP
        chaotic_matrix = self.__acm.encrypt(matrix_of_pixel)
        print(len(chaotic_matrix))

        # TRANSFORMATION
        cipherimage = transform.matrix_to_image(chaotic_matrix)
        print(cipherimage.size)

        # CIPHERIMAGE SAVING
        cipherimage.save(cipherimage_filepath)

    def decrypt(self, cipherimage_filepath, plainfile_filepath):
        from PIL import Image

        cipherimage = Image.open(cipherimage_filepath, mode='r')
        print(cipherimage.size)

        # TRANSFORMATION
        chaotic_matrix = transform.image_to_matrix(cipherimage)
        print(len(chaotic_matrix))

        # ARNOLD'S CAT MAP
        matrix_of_pixel = self.__acm.decrypt(chaotic_matrix)
        print(len(matrix_of_pixel))

        # TRANSFORMATION
        list_of_pixel = transform.matrix_to_pixels(matrix_of_pixel)
        print(len(list_of_pixel))
        randomized_byte = transform.pixels_to_numbers(list_of_pixel)

        # DERANDOMIZED TEXT
        list_of_byte = self.__rt.decrypt(randomized_byte[:-1])

        # TRANSFORMATION
        transform.numbers_to_file(list_of_byte, plainfile_filepath)
