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

    def encrypt(self, plainfile):
        # TRANSFORMATION
        plainbytes = transform.buffer_to_bytes(plainfile)
        plainbytes = transform.pad_bytes(plainbytes)

        # RANDOMIZE TEXT
        cipherbytes = self.__rt.encrypt(plainbytes)

        # TRANSFORMATION
        plainmatrix = transform.bytes_to_matrix(cipherbytes)

        # ARNOLD'S CAT MAP
        ciphermatrix = self.__acm.encrypt(plainmatrix)

        # TRANSFORMATION
        cipherimage = transform.matrix_to_image(ciphermatrix)

        return cipherimage

    def decrypt(self, cipherimage):
        # TRANSFORMATION
        ciphermatrix = transform.image_to_matrix(cipherimage)

        # ARNOLD'S CAT MAP
        plainmatrix = self.__acm.decrypt(ciphermatrix)

        # TRANSFORMATION
        cipherbytes = transform.matrix_to_bytes(plainmatrix)

        # DERANDOMIZED TEXT
        plainbytes = self.__rt.decrypt(cipherbytes)

        # TRANSFORMATION
        plainbytes = transform.strip_bytes(plainbytes)
        plainfile = transform.bytes_to_buffer(plainbytes)

        return plainfile
