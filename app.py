from blocks import acm, bbs, rt, transform


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
        bts = transform.file_to_bytes(plainfile_filepath)
        plainbytes = transform.pad_bytes(bts)

        # RANDOMIZE TEXT
        randomized_bytes = self.__rt.encrypt(plainbytes)

        # TRANSFORMATION
        pixels = transform.compile_bytes_to_pixels(randomized_bytes)
        pixel_matrix = transform.compile_pixels_to_matrix(pixels)

        # ARNOLD'S CAT MAP
        ciphermatrix = self.__acm.encrypt(pixel_matrix)

        # TRANSFORMATION
        cipherimage = transform.matrix_to_image(ciphermatrix)

        # CIPHERIMAGE SAVING
        cipherimage.save(cipherimage_filepath)

    def decrypt(self, cipherimage_filepath, plainfile_filepath):
        from PIL import Image

        cipherimage = Image.open(cipherimage_filepath, mode='r')

        # TRANSFORMATION
        ciphermatrix = transform.image_to_matrix(cipherimage)

        # ARNOLD'S CAT MAP
        pixel_matrix = self.__acm.decrypt(ciphermatrix)

        # TRANSFORMATION
        pixels = transform.decompile_matrix_to_pixels(pixel_matrix)
        randomized_bytes = transform.decompile_pixels_to_bytes(pixels)

        # DERANDOMIZED TEXT
        plainbytes = self.__rt.decrypt(randomized_bytes)

        # TRANSFORMATION
        bts = transform.strip_bytes(plainbytes)
        transform.bytes_to_file(bts, plainfile_filepath)
