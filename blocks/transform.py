from PIL import Image

import numpy as np
import math as mt


def bytes_to_matrix(bts: np.ndarray):
    dimension = int(mt.sqrt((len(bts) // 3)))
    matrix = np.array(bts, np.dtype('B')).reshape(dimension, dimension, 3)

    return matrix


def matrix_to_bytes(matrix: np.ndarray):
    return matrix.reshape(matrix.size)


def matrix_to_image(matrix: np.ndarray):
    image = Image.fromarray(
        matrix
    )

    return image


def image_to_matrix(image: Image):
    return np.array(image)


# PADDING
def pad_bytes(bts: np.ndarray):
    len_bts = bts.size
    len_rdt = len_bts * 2
    len_pixels = mt.ceil(len_rdt / 3)

    # ESTIMASI N matrix
    # ceil untuk mendapatkan jumlah yang diinginkan
    # kita mencari N genap, agar bisa dibagi 2 untuk RDT
    n_matrix = mt.ceil(mt.sqrt(len_pixels))
    if n_matrix % 2 == 1:
        n_matrix += 1

    exp_len_pixels = n_matrix ** 2
    exp_len_rdt = exp_len_pixels * 3
    exp_len_bts = exp_len_rdt // 2

    amount_of_padding = exp_len_bts - len_bts

    padding = np.zeros(amount_of_padding, np.dtype('B'))

    return np.append(bts, padding)


# STRIP
def strip_bytes(bts: np.ndarray):
    to = bts.size

    while bts[to - 1] == 0:
        to -= 1

    return np.delete(bts, np.s_[to:])
