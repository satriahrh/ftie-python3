def file_to_bytes(filepath):
    with open(filepath, 'rb') as fstream:
        byte_array = fstream.read()

    return byte_array


def compile_bytes_to_pixels(bts):
    pixels = []

    for i in range(len(bts) // 3):
        pixels.append((
            bts[3 * i],
            bts[3 * i + 1],
            bts[3 * i + 2],
        ))

    return pixels


def compile_pixels_to_matrix(pixels):
    from math import sqrt

    n_matrix = int(sqrt(len(pixels)))

    matrix = [
        [
            pixels[n_matrix * x + y] for y in range(n_matrix)
        ]
        for x in range(n_matrix)
    ]

    return matrix


def decompile_matrix_to_pixels(matrix):
    pixels = []
    for row in matrix:
        for element in row:
            pixels.append(element)

    return pixels


def decompile_pixels_to_bytes(pixels):
    bts = bytearray()
    for pixel in pixels:
        for number in pixel:
            bts.append(number)

    bts = bytes(bts)
    return bts


def matrix_to_image(matrix):
    from PIL import Image

    image = Image.new(
        size=(len(matrix), len(matrix[0])),
        mode='RGB',
        color=(256, 256, 256)
    )

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            image.putpixel(
                xy=(x, y),
                value=matrix[x][y]
            )

    return image


def image_to_matrix(image):
    matrix = []
    for x in range(image.size[0]):
        matrix.append([])
        for y in range(image.size[1]):
            matrix[x].append(image.getpixel((x, y)))

    return matrix


def bytes_to_file(bts, file_path):
    with open(file_path, "wb") as fstream:
        fstream.write(bts)

    return file_path


# PADDING
def pad_bytes(bts):
    from math import ceil, sqrt

    len_bts = len(bts)
    len_rdt = len_bts * 2
    len_pixels = ceil(len_rdt / 3)

    # ESTIMASI N matrix
    # ceil untuk mendapatkan jumlah yang diinginkan
    # kita mencari N genap, agar bisa dibagi 2 untuk RDT
    n_matrix = ceil(sqrt(len_pixels))
    if n_matrix % 2 == 1:
        n_matrix += 1

    exp_len_pixels = n_matrix ** 2
    exp_len_rdt = exp_len_pixels * 3
    exp_len_bts = exp_len_rdt // 2

    amount_of_padding = exp_len_bts - len_bts

    bts += bytes(amount_of_padding)

    return bts


# STRIP
def strip_bytes(bts):
    to = len(bts)

    while bts[to - 1] == 0:
        to -= 1

    return bts[:to]
