from blocks import acm, bbs, rt, transform


class Application:
    def __init__(
        self,
        p, q, s,
        a, b, n,
    ):
        # BBS
        self.__bbs = bbs.BBS(p=p, q=q, s=s)

        # RT
        self.__rt = rt.RT(self.__bbs)

        # ACM
        self.__acm = acm.ACM(a=a, b=b, n=n)

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
