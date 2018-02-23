def file_to_numbers(file_path):
    numbers = []
    with open(file_path, "rb") as fstream:
        byte = fstream.read(1)
        while byte != b'':
            number = ord(byte)
            numbers.append(number)
            byte = fstream.read(1)

    return numbers


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


def pixels_to_matrix(pixels):
    from math import sqrt
    pixels = pad_pixels(pixels)

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
def pad_numbers(numbers):
    # to be processed in numbers_to_pixels
    from math import ceil

    expected_len_numbers = ceil(len(numbers) / 3) * 3

    for i in range(len(numbers), expected_len_numbers):
        numbers.append(0)

    return numbers


def pad_pixels(pixels):
    # to be processed in pixels_to_matrix
    from math import ceil, sqrt

    expected_len_pixels = int(pow(ceil(sqrt(len(pixels))), 2))

    for i in range(len(pixels), expected_len_pixels):
        pixels.append((0, 0, 0))

    return pixels
