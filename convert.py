from numpy import array
from PIL import Image
from qrcode import QRCode, constants

def generateasciiQR(data, invert=False, white='██', black='  ', version=1, border=1, correction='M'):
    # Parse error correction
    if correction == 'L':
        ecc = constants.ERROR_CORRECT_L
    elif correction == 'Q':
        ecc = constants.ERROR_CORRECT_Q
    elif correction == 'H':
        ecc = constants.ERROR_CORRECT_H
    else: # default M
        ecc = constants.ERROR_CORRECT_M

    # Generate QR code
    qr = QRCode(version=version, box_size=1, border=border, error_correction=ecc)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255))

    image_array = array(image.getdata())
    width = image.size[0]
    height = image.size[1]

    # Get offset
    offset = 0
    while image_array[offset * width + offset][0] == 255:
        offset += 1

    # Get scale
    scale = 1
    while image_array[(offset + scale) * width + (offset + scale)][0] == 0:
        scale += 1

    # Resize
    image = image.resize((width // scale, height // scale), Image.Resampling.NEAREST)
    image_array = array(image.getdata())
    width = image.size[0]
    height = image.size[1]

    # Inverted colors
    if invert:
        image_array = 255 - image_array

    # Generate ASCII art
    ascii_art = []
    
    for i in range(height):
        line = ''
        for j in range(width):
            if image_array[i * width + j][0] < 128:
                line += white
            else:
                line += black
        ascii_art.append(line)

    return '<br>'.join(ascii_art)

# Example usage:

