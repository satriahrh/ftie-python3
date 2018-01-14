from blocks.bbs import BBS


def main():
    # TODO create big prime number recommender
    bbs = BBS(p=7, q=11, s=9)
    if not bbs.validated():
        exit()
    print("BBS is ready")


if __name__ == '__main__':
    main()
