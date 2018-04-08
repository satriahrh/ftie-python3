from PIL import Image


def diff(p: int, c: int):
    return p != c


def npcr(plainimage: Image, cipherimage: Image):
    r, g, b = 0, 0, 0
    T = plainimage.size[0] * plainimage.size[1]
    for i in range(plainimage.size[0]):
        for j in range(plainimage.size[1]):
            p = plainimage.getpixel((i, j))
            c = cipherimage.getpixel((i, j))
            r += (diff(p[0], c[0]))
            g += (diff(p[1], c[1]))
            b += (diff(p[2], c[2]))
    return r / T, g / T, b / T


def uaci(plainimage: Image, cipherimage: Image):
    r, g, b = 0, 0, 0
    T = plainimage.size[0] * plainimage.size[1]
    F = 255
    FT = F * T
    for i in range(plainimage.size[0]):
        for j in range(plainimage.size[1]):
            p = plainimage.getpixel((i, j))
            c = cipherimage.getpixel((i, j))
            r += abs(p[0] - c[0])
            g += abs(p[1] - c[1])
            b += abs(p[2] - c[2])
    return r / FT, g / FT, b / FT
