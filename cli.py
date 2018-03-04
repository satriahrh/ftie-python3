#!/home/hafizhme/code/ftie-rt-acm/venv/bin/python
"""
usage:
    cli <encrypt/decrypt> <input_file> -bbs <config> -acm <acm_config> <-option>

example:
    cli encrypt ptx.pdf -bbs 7 11 9 -acm 1 1 23 -o out.jpg
    cli decrypt ptx.pdf -bbs 7 11 9 -acm 1 1 23

option:
    -bbs    <p> <q> <seed>
    -acm    <a> <b> <n>
    -o      <output file name>
            default <input_file>

"""
import os
from PIL import Image
from blocks.acm import ACM
from blocks.bbs import BBS
from blocks.rt import RT
from blocks import transform

data = {}
state = 0
sub_state = 1
for arg in os.sys.argv[1:]:
    if state == 0:
        if sub_state == 1:
            data['do'] = arg
            sub_state += 1
        elif sub_state == 2:
            if os.path.exists(arg):
                data['input_file'] = arg
                data['output_file'] = arg
            else:
                print(f'ERROR: {arg} not found')
                exit()
            state, sub_state = 0, 0
        elif sub_state == 0:
            if arg == '-bbs':
                data['bbs'] = {}
                state = 1
            elif arg == '-acm':
                data['acm'] = {}
                state = 2
            elif arg == '-o':
                data['output_file'] = ''
                state = 3
    elif state == 1:
        if sub_state == 0:
            data['bbs']['p'] = int(arg)
            sub_state += 1
        elif sub_state == 1:
            data['bbs']['q'] = int(arg)
            sub_state += 1
        elif sub_state == 2:
            data['bbs']['seed'] = int(arg)
            state, sub_state = 0, 0
    elif state == 2:
        if sub_state == 0:
            print(arg)
            data['acm']['a'] = int(arg)
            sub_state += 1
        elif sub_state == 1:
            data['acm']['b'] = int(arg)
            sub_state += 1
        elif sub_state == 2:
            data['acm']['n'] = int(arg)
            state, sub_state = 0, 0

    elif state == 3:
        data['output_file'] = arg
        state = 0
        state = 0


if data['do'] == 'encrypt':
    # ENCRYPT
    numbers = transform.file_to_numbers(data['input_file'])
    bbs = BBS(data['bbs']['p'], data['bbs']['q'], data['bbs']['seed'])
    rt = RT(bbs)
    rt_out = rt.encrypt(numbers)
    pixels = transform.numbers_to_pixels(rt_out)
    matrix = transform.pixels_to_matrix(pixels)
    acm = ACM(data['acm']['a'], data['acm']['b'], len(matrix))
    matrix = acm.encrypt(matrix, data['acm']['n'])
    image = transform.matrix_to_image(matrix)
    if data['output_file'][-3:].lower() != 'bmp':
        data['output_file'] += '.bmp'
    image.save(data['output_file'], format='bmp')
elif data['do'] == 'decrypt':
    # DECRYPT
    image = Image.open(data['input_file'])  # SAMPLE
    matrix = transform.image_to_matrix(image)
    acm = ACM(data['acm']['a'], data['acm']['b'], len(matrix))
    matrix = acm.decrypt(matrix)
    pixels = transform.matrix_to_pixels(matrix, data['acm']['n'])
    numbers = transform.pixels_to_numbers(pixels)
    bbs = BBS(data['bbs']['p'], data['bbs']['q'], data['bbs']['seed'])
    rt = RT(bbs)
    numbers = rt.decrypt(numbers)

    transform.numbers_to_file(numbers, data['output_file'])
else:
    print('Syntax invalid')
