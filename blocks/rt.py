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
