# this mini experiment is used to calculate size of plaintext

def plaintext_by_maps_dimension(maps_dimension):
    return maps_dimension ** 2 * 3 / 2

def plaintext_by_size(max_file_size):
    maps_dimension = 2
    size = plaintext_by_maps_dimension(maps_dimension)
    while size <= max_file_size:
        new_maps_dimension = maps_dimension + 2
        new_size = plaintext_by_maps_dimension(new_maps_dimension)
        print(new_maps_dimension, new_size)
        maps_dimension = new_maps_dimension
        size = new_size
    print('The result is N={}, for |P|={}'.format(maps_dimension, int(size)))
    return maps_dimension, int(size)


if __name__ == "__main__":
    MAX_FILE_SIZE = 26214400
    MAPS_DIMENSION, SIZE = plaintext_by_size(MAX_FILE_SIZE)  # in byte = 25 MB
    print(f'difference {abs(SIZE - MAX_FILE_SIZE)}')
