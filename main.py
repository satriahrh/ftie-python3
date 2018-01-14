from blocks.bbs import BBS


def main_bbs():
    # BLUM BLUM SHUB
    # TODO create big prime number recommender
    p, q, s = 7, 11, 9
    bbs = BBS(p, q, s)

    if not bbs.validated():
        exit()

    first_number = bbs.next()
    second_number = bbs.next()

    print("{:^35}".format("BBS Keystream Generator"))
    print("> Using p={}, q={}, s={}".format(p, q, s))
    print("> {:8}number : {}".format("First", first_number))
    print("> {:8}number : {}".format("Second", second_number))


if __name__ == '__main__':
    main_bbs()
