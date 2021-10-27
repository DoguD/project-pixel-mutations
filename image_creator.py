import numpy as np
from PIL import Image
import time


def read_dna(path):
    f = open(path, 'r')
    return f.read()


def generate_image(dna_path):
    dna = read_dna(dna_path)
    print("DNA to be processed: " + dna)

    # Create canvas
    image_dimensions = (128, 128, 3)
    image_array = np.zeros(image_dimensions, dtype=np.uint8)
    # Make everything white on array
    for i in range(image_dimensions[1]):
        for j in range(image_dimensions[0]):
            image_array[j][i] = [255, 255, 255]
    cursor_position = [0, 0]

    # Images Array
    images = []

    index = 0
    # Process DNA
    for c in dna:
        # MOVE OPERATORS
        new_cursor_x = cursor_position[1]
        new_cursor_y = cursor_position[0]

        if c == 'u':
            new_cursor_y -= 1
            if new_cursor_y < 0:
                new_cursor_y += image_dimensions[0]
        if c == 'd':
            new_cursor_y += 1
            if new_cursor_y >= image_dimensions[0]:
                new_cursor_y -= image_dimensions[0]
        if c == 'r':
            new_cursor_x += 1
            if new_cursor_x >= image_dimensions[1]:
                new_cursor_x -= image_dimensions[1]
        if c == 'l':
            new_cursor_x -= 1
            if new_cursor_x < 0:
                new_cursor_x += image_dimensions[1]
        # Assign new positions
        cursor_position = [new_cursor_y, new_cursor_x]

        # PAINT OPERATORS
        if c == 'p':
            image_array[new_cursor_y, new_cursor_x] = [0, 0, 0]
        elif c == 'e':
            print("Cell painted to white.")
            image_array[new_cursor_y, new_cursor_x] = [255, 255, 255]

        # If paint operation done append to array
        if c == 'p' or c == 'e':
            images.append(Image.fromarray(image_array))
            index += 1

    # STATIONARY IMAGE START
    '''
    # Create a PIL image
    img = Image.fromarray(image_array)
    img.show()
    '''
    # STATIONARY IMAGE END
    print("Will save GIF | Frame Count: " + str(index))
    # Save GIF
    images[0].save('./out/output.gif',
                   save_all=True, append_images=images[1:], optimize=False, duration=10, loop=0)
    # Save Stationary Version
    images[-1].save('./out/output.png')


generate_image('./gen0_dnas/0.txt')
