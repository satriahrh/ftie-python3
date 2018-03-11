from errors import ValidationError

def file_to_bytes(filepath):
    with open(filepath, 'rb') as fstream:
        byte_array = fstream.read()

    return byte_array


def compile_bytes_to_pixels(bts):
    pixels = []

    for i in range(int(len(bts) / 3)):
        pixels.append((
            bts[3 * i],
            bts[3 * i + 1],
            bts[3 * i + 2],
        ))

    return pixels


def compile_pixels_to_matrix(pixels):
    from math import sqrt

    n_matrix = sqrt(len(pixels))
    # TODO create unittest for this raise
    if n_matrix % 1 != 0:
        raise ValidationError(
            "Try another pixels",
            "len(pixels) is not a quadratic number"
        )

    n_matrix = int(n_matrix)

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


def numbers_to_pixels(numbers):
    numbers = pad_numbers(numbers)

    pixels = []
    for i in range(int(len(numbers) / 3)):
        pixels.append((
            numbers[3 * i],
            numbers[3 * i + 1],
            numbers[3 * i + 2],
        ))

    return pixels


def pixels_to_matrix(pixels, n_matrix=None):
    from math import sqrt
    len_pixels = None

    if n_matrix is not None:
        len_pixels = int(n_matrix ** 2)
        pixels = pad_pixels(pixels, len_pixels)
    else:
        pixels = pad_pixels(pixels, len_pixels)
        n_matrix = int(sqrt(len(pixels)))

    matrix = [
        [
            pixels[n_matrix * x + y] for y in range(n_matrix)
        ]
        for x in range(n_matrix)
    ]

    return matrix


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


def matrix_to_pixels(matrix):
    pixels = []
    for row in matrix:
        for element in row:
            pixels.append(element)

    return pixels


def pixels_to_numbers(pixels):
    numbers = []
    for pixel in pixels:
        for number in pixel:
            numbers.append(number)

    return numbers


def numbers_to_file(numbers, file_path):
    with open(file_path, "wb") as fstream:
        for number in numbers:
            fstream.write(number.to_bytes(1, "little", signed=False))

    return file_path


# PADDING
def pad_bytes(bts):
    from math import ceil, sqrt

    len_bts = len(bts)
    len_rdt = len_bts * 2

    n_matrix = ceil(sqrt(len_rdt / 3))
    if n_matrix % 2 == 1:
        n_matrix += 1

    amount_of_padding = ceil(
        (
            (n_matrix ** 2) * 3
            - len_rdt
        ) / 2
    )

    bts += bytes(amount_of_padding)

    return bts


def pad_numbers(numbers):
    # to be processed in numbers_to_pixels
    from math import ceil

    # to make the original numbers do not get populated
    numbers = numbers.copy()

    expected_len_numbers = ceil(len(numbers) / 3) * 3

    numbers += [0 for i in range(len(numbers), expected_len_numbers)]

    return numbers


def pad_pixels(pixels, expected_len_pixels=None):
    # to be processed in pixels_to_matrix
    from math import ceil, sqrt

    # to make the original pixels do not get populated
    pixels = pixels.copy()

    if expected_len_pixels is None:
        expected_len_pixels = int(pow(ceil(sqrt(len(pixels))), 2))

    pixels += [(0, 0, 0) for i in range(len(pixels), expected_len_pixels)]

    return pixels


# STRIP
def strip_bytes(bts):
    to = len(bts)

    while bts[to - 1] == 0:
        to -= 1

    return bts[:to]
