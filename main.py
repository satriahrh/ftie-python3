from blocks.bbs import BBS


def main_bbs():
    # BLUM BLUM SHUB
    # TODO create big prime number recommender
    bbs = BBS(_p=7, _q=11, seed=9)

    if not bbs.validated():
        exit()

    first_number = bbs.next()
    second_number = bbs.next()

    print("{:^35}".format("BBS Keystream Generator"))
    print("> Using p={}, q={}, s={}".format(7, 11, 9))  # TODO remove hardcoded
    print("> {:8}number : {}".format("First", first_number))
    print("> {:8}number : {}".format("Second", second_number))


# TODO add acm usage
# TODO add rt usage
if __name__ == '__main__':
    main_bbs()
