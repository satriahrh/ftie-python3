#!/home/hafizhme/code/ftie-rt-acm/venv/bin/python
"""
usage:
    cli <encrypt/decrypt> <input_file> -bbs <config> -acm <acm_config> <-option>

example:
    cli encrypt ptx.pdf -bbs 7 11 9 -acm discreete -o out.jpg
    cli decrypt ptx.pdf -bbs 7 11 9 -acm discreete

option:
    -bbs    <p> <q> <seed>
    -acm    <acm_type:>
                discreete   <no_additional config>
    -o      <output file name>
            default <input_file>

"""
from PIL import Image
from blocks.acm import ACM
from blocks.bbs import BBS
from blocks.rt import RT
from blocks import transform

bbs_1 = BBS(_p=7, _q=11, seed=9)
bbs_2 = BBS(_p=7, _q=11, seed=9)
rt_1 = RT(bbs_1)
rt_2 = RT(bbs_2)


# ENCRYPT
filepath = 'telo.pdf'  # SAMPLE
numbers = transform.file_to_numbers(file_path=filepath)
rt_out = rt_1.encrypt(numbers)
pixels = transform.numbers_to_pixels(rt_out)
matrix = transform.pixels_to_matrix(pixels)
acm = ACM(1, 1, len(matrix))
matrix = acm.encrypt(matrix)
image = transform.matrix_to_image(matrix)
image.save('telo.jpg', format='bmp')

# DECRYPT
image = Image.open('telo.jpg')  # SAMPLE
matrix = transform.image_to_matrix(image)
acm = ACM(1, 1, len(matrix))
matrix = acm.decrypt(matrix)
pixels = transform.matrix_to_pixels(matrix)
numbers = transform.pixels_to_numbers(pixels)
numbers = rt_2.decrypt(numbers)
transform.numbers_to_file(numbers=numbers, file_path='telotelo.pdf')
