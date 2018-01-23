class RT:
    def __init__(self, bbs):
        """
        INPUT
        bbs         blocks.bbs.BBS
        """
        self.__errors = {}
        self.__validate(bbs)
        if self.validated():
            self.__bbs = bbs

    def get_errors(self, key=None):
        try:
            if key:
                return self.__errors[key]
            return self.__errors
        except KeyError:
            return ""

    def __validate(self, bbs):
        self.__validated = False
        if not bbs.validated():
            bbs_errors = bbs.get_errors('validation')
            self.__errors['validation'] = \
                f"BBS is not validated: {bbs_errors}"
            return

        self.__validated = True

    def validated(self):
        return self.__validated

    def encrypt(self, P):
        """
        INPUT
        P   [int 0...N-1]
        OUTPUT
        C   [int 0...2N-2]
        """
        from random import randint
        C = []
        for p in P:
            r = randint(0, 256)
            k = self.__bbs.next()
            C.append(
                (k + 2 * p + r) % 256
            )
            C.append(
                (2 * k + p + r) % 256
            )

        return C

    def decrypt(self, C):
        """
        INPUT
        C   [int 0...2N-2]
        OUTPUT
        P   [int 0...N-1]
        """
        P = []
        for i in range(int(len(C) / 2)):
            k = self.__bbs.next()
            P.append(
                (C[2 * i] - C[2 * i + 1] + k) % 256
            )

        return P
